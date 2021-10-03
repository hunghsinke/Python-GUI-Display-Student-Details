#import tkinter
from tkinter import *

#start the window
#set window title and size
root = Tk()
root.title('Student Details')
root.geometry('800x400')

#student ID label
st_ID_Label = Label(root, text = 'Student ID')
st_ID_Label.grid(row = 0, column = 0)
#student ID entry
st_ID_entry= Entry(root, width = 10, borderwidth = 5) #entry widget
st_ID_entry.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady = 10)

#student name label
st_name_Label = Label(root, text = 'Student name')
st_name_Label.grid(row = 0, column = 6)

#student name entry
st_name_entry = Entry(root, width = 10, borderwidth = 5)
st_name_entry.grid(row = 0, column = 7, columnspan = 3, padx = 10, pady = 10)

#display the items in the listbox
display_entry = Entry(root,width = 50, borderwidth = 5 )
display_entry.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady=10)



#define display info function
#get entry from student name
#get entry from student ID
def display_info():
    st_ID = st_ID_entry.get()
    st_name = st_name_entry.get()
    display_entry.insert(0, 'Your student ID is: '+str(st_ID) +'\t'
                         +'Your name is: '+ str(st_name))


#display the selected listbox item
def showSelected():

    #show.config(text='My name is '+st_name+'My student ID is '+st_ID+'My hobby is: '+listbox.get(ANCHOR))
    show.config(text= 'My hobby is: ' + listbox.get(ANCHOR))


#display the name and student id in entry box
display_button = Button(root, text = 'Display details', padx= 40, pady = 20, command = display_info)
display_button.grid(row = 1, column = 0)


#display the entries in the listbox
#define a listbox, put three hobbies in it for user to choose
#when the user chose, get the items
lbl = Label(root,text = "A list of hobbies...")

#initial listbox to allow selection
listbox = Listbox(root)

#hobbies list
listbox.insert(1, "Running")

listbox.insert(2, "Swimming")

listbox.insert(3, "Horse Riding")

listbox.insert(4, "Bushwalking")

#button to display hobbies
btn = Button(root, text="Show Selected", command=showSelected)

#position of the label of listbox
lbl.grid(row = 3, column = 0)

#position of the listbox
listbox.grid(row = 3, column = 1)

#position of the button
btn.grid(row = 4, column = 0)

#position of the display text
show = Label(root)
show.grid(row = 4, column = 1)


#start mainloop
root.mainloop()
