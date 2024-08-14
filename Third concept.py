from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to quit the program
def quit_program():
    """
    Close the main window when the "Quit" button is clicked
    """
    main_window.destroy()

# Function to print all customer details
def print_customer_details():
    """
    Print all customer details in the GUI
    """
    name_count=0

    for widget in main_window.grid_slaves(row=8):
        widget.destroy()
    if not customer_details:
        messagebox.showerror("No Entries", "Nothing is filled in to display")
        return
    name_count=0
    # Create column headings
    Label(main_window,font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window,font=("Helvetica 10 bold"),text="Customer Name").grid(column=1,row=7)
    Label(main_window,font=("Helvetica 10 bold"),text="Receipt Number").grid(column=2,row=7)
    Label(main_window,font=("Helvetica 10 bold"),text= "Item Hired").grid(column=3,row=7)
    Label(main_window,font=("Helvetica 10 bold"),text="Quantity").grid(column=4,row=7)
    # Add each item in the list to its own row
    while name_count<counters['total_entries']:
        Label(main_window,text=name_count).grid(column=0, row=name_count+8)
        Label(main_window,text=customer_details[name_count][0]).grid(column=1,row=name_count+8)
        Label(main_window,text=customer_details[name_count][1]).grid(column=2,row=name_count+8)
        Label(main_window,text=customer_details[name_count][2]).grid(column=3,row=name_count+8)
        Label(main_window,text=customer_details[name_count][3]).grid(column=4,row=name_count+8)
        name_count+=1
    counters['name_count']=name_count
    

# Function to check input validity
def check_inputs():
    """
    Check if all input fields are valid before adding to the list
    """
    input_check=0

    # Clear error messages
    for i in range(4):
        Label(main_window,text=" ").grid(column=2,row=i)
    # Check if customer name is not blank
    if len(entry_customer.get())==0:
        messagebox.showerror("Name error","Required")
        input_check =1
    elif not entry_customer.get().isalpha():
        messagebox.showerror("Name error","Enter your name and no spaces")
        input_check=1
    # Check if item hired is not blank
    if item_Variable.get()=="Choose Item":
        messagebox.showerror("Item error","Enter selcet your item")
        input_check=1
    # Check if quantity is not blank and between 1 and 500
    quantity=entry_quantity.get()
    if len(quantity)==0:
        messagebox.showerror("Quantity error","Quantity is Required")
    elif not quantity.isdigit():
        messagebox.showerror("Quantity error","Number is Required")
    else:
        quantity_value=int(quantity)
        if quantity_value<1 or quantity_value>500:
            messagebox.showerror("Quantity error","Quantity must be between 1 and 500")
            input_check=1

    # If all inputs are valid, add to the list
    if input_check==0:
        append_name()

# Function to add a new receipt to the list
def append_name():
    """
    Add a new item to the list and clear input fields
    """
    global receipt_number
    customer_details.append([entry_customer.get(),receipt_number,item_Variable.get(),entry_quantity.get()])
    # Clear input fields
    entry_customer.delete(0,'end')
    item_Variable.set("")
    entry_quantity.delete(0,'end')
    counters['total_entries']+=1
    receipt_number=random.randint(100000, 999999)

# Function to delete a row from the list
def delete_row():
    """
    Delete a row from the list and update the GUI
    """
    delete=int(delete_item.get())
    if 0<=delete<len(customer_details):
        del customer_details[delete]
        counters["total_entries"]-=1
        delete_item.delete(0, 'end')
        for widget in main_window.grid_slaves(row=delete+8):
            widget.destroy()
        print_customer_details
# Create the buttons and labels
def setup_buttons():
    """
    Create all the buttons and labels for the GUI
    """
    global item_Variable,item_cbox
    item_Variable=StringVar()
    item_Variable.set("")
    item_cbox=ttk.Combobox(main_window,textvariable=item_Variable,values=Party_items)
    item_cbox.grid(column=1,row=1)

    Label(main_window, text="Customer Name",font=("Calibri",9,"bold")).grid(column=0,row=0,sticky=E)
    Label(main_window, text="Item Hired",font=("Calibri",9,"bold")).grid(column=0,row=1,sticky=E)
    Label(main_window, text="Quantity",font=("Calibri",9,"bold")).grid(column=0,row=2,sticky=E)
    Label(main_window, text="Row #",font=("Calibri",9,"bold")).grid(column=3,row=2,sticky=E)
    image_3=Image.open('pic4.png')
    image_3=image_3.resize((30,30))   
    img_3=ImageTk.PhotoImage(image_3)
    button3=Button(main_window,text="Quit",font=("Calibri",9,"bold"),bg='red',command=quit_program,width=100,image=img_3,compound='left')
    button3.image=img_3
    button3.grid(column=4,row=0,sticky=E)
    image=Image.open('pic1.png')
    image=image.resize((30,30))
    img=ImageTk.PhotoImage(image)
    button=Button(main_window,text="Submit",font=("Calibri",9,"bold"),command=check_inputs,image=img,compound='left')
    button.image=img 
    button.grid(column=3,row=1)
    image_1=Image.open('pic2.png')
    image_1=image_1.resize((30,30))
    img_1=ImageTk.PhotoImage(image_1)
    button1=Button(main_window,text="Print Details",font=("Calibri",9,"bold"),command=print_customer_details,width=100,image=img_1,compound='left')
    button1.image=img_1
    button1.grid(column=4,row=1,sticky=E)
    image_2=Image.open('pic3.png')
    image_2=image_2.resize((30, 30))
    img_2=ImageTk.PhotoImage(image_2)
    button2=Button(main_window,text="Delete Row",font=("Calibri",9,"bold"),command=delete_row,width=100,image=img_2,compound='left')
    button2.image=img_2
    button2.grid(column=4,row=3,sticky=E)

    items=[" "]

Party_items=["spoons","balloons","party poppers","ribbons","confetti","party hat"]

counters={'total_entries':0,'name_count':0} # initialize counters for number of entries and names
customer_details=[] # create an empty list to store customer details
receipt_number=random.randint(100000,999999) # generate a random receipt number
# Start the program
def main():
    """
    Start the GUI
    """
    setup_buttons()
    main_window.title("Julies party store")
    main_window.mainloop()

# Create empty list for customer details and empty variable for entries in the list

main_window=Tk() # create the main window
main_window.geometry("600x300")
bg = PhotoImage(file="pic10.png") 
# Show image using label 
label1=Label( main_window,image=bg) 
label1.place(x=0,y=0) 
entry_customer=Entry(main_window) # create a entry box for customer name
entry_customer.grid(column=1, row=0)
entry_hired=Entry(main_window) # create a entry box for item hired
entry_hired.grid(column=1,row=1)
entry_quantity=Entry(main_window) # create a entry box for quantity
entry_quantity.grid(column=1,row=2)
delete_item=Entry(main_window) # create a entry box for deleting rows
delete_item.grid(column=3,row=3)
main()
