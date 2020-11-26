#Creating a window
from tkinter import *
from random import sample
from tkinter import messagebox
import random

def generatedNumbers():
    num1.configure(text=str(random.sample(range(1, 49),1)))
    num2.configure(text=str(random.sample(range(1, 49), 1)))
    num3.configure(text=str(random.sample(range(1, 49), 1)))
    num4.configure(text=str(random.sample(range(1, 49), 1)))
    num5.configure(text=str(random.sample(range(1, 49), 1)))
    num6.configure(text=str(random.sample(range(1, 49), 1)))

def die():
    num1.configure(text=str(0))
    num2.configure(text=str(0))
    num3.configure(text=str(0))
    num4.configure(text=str(0))
    num5.configure(text=str(0))
    num6.configure(text=str(0))

#Creating a window
window = Tk()
window.title("6 Figure Lottery!!!")
window.resizable(1000, 2000)
#creating the label
lblEnter= Label(window, text="Press play before playing then enter 6 Numbers!")
lblEnter.grid(row=0,column=1)
#creating the entries
def playing():
    try:
        entryNum1 = Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey',justify='center')
        entryNum1.grid(row = 1, column = 1, padx = 5, pady = 7)
        entryNum2 = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',justify='center')
        entryNum2.grid(row = 1, column = 2, padx = 5, pady = 7)
        entryNum3 = Entry(window, relief='groove', width = 5, bd=4, fg='white' ,bg='grey',justify='center')
        entryNum3.grid(row = 1, column = 3, padx = 5, pady = 7)
        entryNum4 = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',justify='center')
        entryNum4.grid(row = 1, column = 4, padx = 5, pady = 7)
        entryNum5 = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',justify='center')
        entryNum5.grid(row = 1, column = 5, padx = 5, pady = 7)
        entryNum6 = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',justify='center')
        entryNum6.grid(row = 1, column = 6, padx = 5, pady = 7)
    except TypeError:
        messagebox.showinfo("Error message","Please enter a number")

# label.config(text=str())
#creating the labels
enterNum= Label(window, text="Lottery Numbers!")
enterNum.grid(row=7,column=1)
num1 = Label(window, relief='groove', width = 5, bd=14, text="0", fg='white', bg='grey')
num1.grid(row = 8, column = 1, padx = 5, pady = 7)
num2 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='grey')
num2.grid(row = 8, column = 2, padx = 5, pady = 7)
num3 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='grey')
num3.grid(row = 8, column = 3, padx = 5, pady = 7)
num4 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='grey')
num4.grid(row = 8, column = 4, padx = 5, pady = 7)
num5 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='grey')
num5.grid(row = 8, column = 5, padx = 5, pady = 7)
num6 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='white', bg='grey')
num6.grid(row = 8, column = 6, padx = 5, pady = 7)

def compare():
    pass
#Creating a button
#Close
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = 'grey')
closeButton.grid(row = 10, column = 1, columnspan = 6, pady = 7)
#Generate Numbers
numberGen = Button(window, width=20, text="compare", command=compare)
numberGen.configure(fg = "White" ,bg = "navy")
numberGen.grid(row = 9, column = 1, padx = 5, pady = 7)
#Reset
reset = Button(window, width=10, text="Reset", command =die)
reset.configure(fg = "White" ,bg = "navy")
reset.grid(row = 9, column = 2, padx = 5, pady = 7)

play = Button(window, width=10, text="Play", command =playing)
play.configure(fg = "White" ,bg = "navy")
play.grid(row = 9, column = 3, padx = 5, pady = 7)

#defining a function to close the program
def close():
    # conformation message, do you really want to exit the program
	sure=messagebox.askyesno(title="Alert",message="Are you sure you want to exit?")
    # if the user clicks yes which means he/she wants to exit the program then the program is closed
	if sure==True:
		window.destroy()
    # if the user clicks no, the program won't exit
	else:
		return None



#attaching the "close" function to the "close" button
closeButton.configure(command = close)

#This is the line that runs the program until you exit
window.mainloop()
