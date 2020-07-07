from tkinter import *
import backend
#select the row 
def get_selected_row(event):
    global selected_tuple   #global variable
    index=l1.curselection()[0]
    selected_tuple=l1.get(index)
    e1.delete(0,END)    # 0 to end 
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)   
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)    
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)    
    e4.insert(END,selected_tuple[4])

def view_command():
    l1.delete(0,END)
    for row in backend.view():
        l1.insert(END,row)
def search_command():
    l1.delete(0,END)
    for row in backend.search(title.get(),author.get(),year.get(),isbn.get()):
        l1.insert(END,row)
def add_command():
    backend.insert(title.get(),author.get(),year.get(),isbn.get())
    l1.delete(0,END)
    l1.insert(END,(title.get(),author.get(),year.get(),isbn.get()))

def delete_command():
    backend.delete(selected_tuple[0])  

def update_command():
    backend.update(selected_tuple[0],title.get(),author.get(),year.get(),isbn.get())

window=Tk()
window.wm_title("Book Library") #Title of the app
#All labels
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
#4 Input
title=StringVar()
e1=Entry(window, textvariable=title)
e1.grid(row=0,column=1)

author=StringVar()
e2=Entry(window, textvariable=author)
e2.grid(row=0,column=3)

year=StringVar()
e3=Entry(window, textvariable=year)
e3.grid(row=1,column=1)

isbn=StringVar()
e4=Entry(window, textvariable=isbn)
e4.grid(row=1,column=3)
#output which will showed in a box
l1=Listbox(window,height=6,width=35)
l1.grid(row=2,column=0,rowspan=6,columnspan=2)
#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#configure
l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)
l1.bind('<<ListboxSelect>>',get_selected_row)
#all buttons
b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()