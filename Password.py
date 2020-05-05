# Python program to generate random 
# password using Tkinter module 
import random 
import pyperclip 
import mysql.connector as con
from mysql.connector import Error
from tkinter import *
from tkinter.ttk import *
  
# Function for calculation of password 
def low(): 
    entry.delete(0, END) 
  
    # Get the length of passowrd 
    length = var1.get() 
  
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = "" 
  
    # if strength selected is low 
    if var.get() == 1: 
        for i in range(0, length): 
            password = password + random.choice(lower) 
        return password 
  
    # if strength selected is medium 
    elif var.get() == 0: 
        for i in range(0, length): 
            password = password + random.choice(upper) 
        return password 
  
    # if strength selected is strong 
    elif var.get() == 3: 
        for i in range(0, length): 
            password = password + random.choice(digits) 
        return password 
    else: 
        print("Please choose an option") 
  
  
# Function for generation of password 
def generate(): 
    password1 = low() 
    entry.insert(10, password1) 
    a=entry.get()	
    b=un.get()
	
    try:
			   connection = con.connect(host='localhost',
										 database='generator',
										 user='root',
										 password='')

			   sql_insert_query = """ INSERT INTO `gen` VALUES (%s,%s)"""						  
			   val=(a,b)		   
			   cursor = connection.cursor()
			   result  = cursor.execute(sql_insert_query,val)
			   records = cursor.fetchall()
			   print ("Record inserted successfully into employee table")
    except Error as error :
	      #rollback if any exception occured
		   print("Failed inserting record into Password table ".format(error))

def show():
		d=u.get()
	
		try:
				   connection = con.connect(host='localhost',
											 database='generator',
											 user='root',
											 password='')

				   sql_insert_query = """ SELECT pass from `gen` where user=%s"""
				   user=(d,)
				   cursor = connection.cursor()
				   cursor.execute(sql_insert_query,user)
				   rec = cursor.fetchall()
				   for row in rec:
					    print(row[0])
				   
			
			
				  
		except Error as error :
			  #rollback if any exception occured
			   print("Failed to display record fromm Password table ".format(error))		   
			
	

  
  
# Function for copying password to clipboard 
def copy1(): 
    random_password = entry.get() 
    pyperclip.copy(random_password) 
	
def new_winF(): # new window definition
	global c,u
	c=StringVar()
	newwin = Toplevel(root)
	use= Label(newwin, text="Username") 
	use.grid(row=0,column=0) 
	u= Entry(newwin,textvariable = c) 
	u.grid(row=0, column=1)
	show_button = Button(newwin, text="Show Passwords", command=show)	
	show_button.grid(row=4, column=2) 
	
	
    
	

  
  
# Main Function 
  

# create GUI window 
root = Tk() 
var = IntVar() 
var1 = IntVar() 
  
# Title of your GUI window 
root.title("Random Password Generator") 
v = StringVar()
# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1)
usern = Label(root, text="Enter Username") 
usern.grid(row=3) 
un= Entry(root,textvariable = v) 
un.grid(row=3, column=1)



  
# create label for length of password 
c_label = Label(root, text="Length") 
c_label.grid(row=1) 
  
# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=3) 
search =Button(root, text ="Search a Password",command=new_winF) 
search.grid(row=5,column=1)





  
# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1) 
  
# Combo Box for length of your password 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 
  
# start the GUI 
root.mainloop() 
