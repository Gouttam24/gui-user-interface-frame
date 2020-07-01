from tkinter import *
import tkinter as tk
import psycopg2

root = Tk( )

def get_data(Name,Age,Address):  # it is created for save user input through gui window into database.
    
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="1234",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''Insert into Student(Name,Age,Address) Values(%s,%s,%s);'''
    cur.execute(query,(Name,Age,Address))
    print("Data inserted")
    conn.commit()
    conn.close()

def search(id): # this function is use for search id and print .
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="1234",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''Select * from Student where id=%s'''
    cur.execute(query,(id))
    row = cur.fetchone()
    
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row): #this function is use for search id and print in frame window.
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END,row)


canvas = Canvas(root,width = 900, height = 480) # it is for createing canvas/windows size.
canvas.pack( )

frame = Frame( )
frame.place(relx =0.3,rely =0.1,relwidth =0.8,relheight = 0.8)

lable = Label(frame,text = "Add Data") # it is for createing Heading.
lable.grid(row =0,column =1)

lable = Label(frame,text = "Name") # create name, age , address heading.
lable.grid(row =2,column =0)
entry_name = Entry(frame) # it is code for make entry field box in frame.
entry_name.grid(row =2, column =1)

lable = Label(frame,text = "Age")
lable.grid(row =3, column =0)
entry_age = Entry(frame)
entry_age.grid(row =3, column =1)


lable = Label(frame,text = "Address")
lable.grid(row =4,column =0)
entry_address = Entry(frame)
entry_address.grid(row =4, column =1)

button = Button(frame,text = "Submit",command = lambda:get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row =5, column =1)

lable = Label(frame,text = "Search")
lable.grid(row =6,column =1)
 
lable = Label(frame,text = "Search By Id")
lable.grid(row =7,column =0)
entry_idsearch =Entry(frame)
entry_idsearch.grid(row =7, column=1)

button = Button(frame,text="Search",command= lambda:search(entry_idsearch.get()))
button.grid(row =7,column=2)

root.mainloop()