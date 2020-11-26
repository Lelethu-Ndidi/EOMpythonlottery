#Creating a window
from tkinter import *
from random import sample
from tkinter import messagebox
import random


#Creating a window
window = Tk()
window.title("6 Figure Lottery!!!")
window.resizable(1000, 2000)

lblEnter= Label(window, text="Press play before playing then enter 6 Numbers!")
lblEnter.grid(row=0,column=1)
entry1= StringVar()
a= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey', textvariable=entry1,justify="center")
a.grid(row = 1, column = 1, padx = 5, pady = 7)
entry2= StringVar()
b= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry2,justify="center")
b.grid(row = 1, column = 2, padx = 5, pady = 7)
entry3= StringVar()
c= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry3,justify="center")
c.grid(row = 1, column = 3, padx = 5, pady = 7)
entry4= StringVar()
d= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry4,justify="center")
d.grid(row = 1, column = 4, padx = 5, pady = 7)
entry5= StringVar()
e= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry5,justify="center")
e.grid(row = 1, column = 5, padx = 5, pady = 7)
entry6= StringVar()
f= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry6,justify="center")
f.grid(row = 1, column = 6, padx = 5, pady = 7)

lottoNumbers = []
def generatedNumbers():
    num1.configure(text=str(random.sample(range(1, 49),1)))
    num2.configure(text=str(random.sample(range(1, 49), 1)))
    num3.configure(text=str(random.sample(range(1, 49), 1)))
    num4.configure(text=str(random.sample(range(1, 49), 1)))
    num5.configure(text=str(random.sample(range(1, 49), 1)))
    num6.configure(text=str(random.sample(range(1, 49), 1)))
    number = random.randint(1,50)
    # while number in lottoNumbers:
    #     # ... if it has, pick a new number instead
    #     number = random.randint(1,50)
    #
    #     #Now that we have a unique number, let's append it to our list.
    #     lottoNumbers.append(number)
    #
    #     #Sort the list in ascending order
    #     lottoNumbers.sort()

#     lotteryNumbers = []
#
# for i in range (0,6):
#   number = random.randint(1,50)
#   #Check if this number has already been picked and ...
#   while number in lotteryNumbers:
#     # ... if it has, pick a new number instead
#     number = random.randint(1,50)
#
#   #Now that we have a unique number, let's append it to our list.
#   lotteryNumbers.append(number)
#
# #Sort the list in ascending order
# lotteryNumbers.sort()

myNumbers = []
def userEntries():
    #creating the entries
    try:
        while True :
            a=int(a.get())
            if a == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
                continue
            elif a < 50 :
                break
        messagebox.showinfo("Error message","Please enter a number from 1 to 49.")

        while True :
            b=int(a.get())
            if b == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
                continue
            elif b == a :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif b < 50 :
                break
            messagebox.showinfo("Error message","Please enter a number from 1 to 45.")

        while True :
            c=int(a.get())
            if c == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
            elif c == a :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif c == b :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif c < 50 :
                break
            messagebox.showinfo("Error message","Please enter a number from 1 to 49.")

        while True :
            d=int(a.get())
            if d == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
                continue
            elif d == a :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif d == b :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif d == c :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif d < 46 :
                break
            messagebox.showinfo("Error message","Please enter a number from 1 to 45.")

        while True :
            e=int(a.get())
            if e == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
                continue
            elif e == a :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif e == b :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif e == c :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif e == d :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif e < 50 :
                break
            messagebox.showinfo("Error message","Please enter a number from 1 to 45.")

        while True :
            f=int(a.get())
            if f == 0 :
                messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
                continue
            elif f == a :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif f == b :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif f == c :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif f == d :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif f == e :
                messagebox.showinfo("Error message","Do not duplicate numbers! Please re-enter.")
                continue
            elif f < 50 :
                messagebox.showinfo("--------------------------------------------------------")
                break
        messagebox.showinfo("Please enter a number from 1 to 49.")

    except TypeError:
        messagebox.showinfo("Error message","Please enter a number")

#creating the label
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



#Creating a button


#defining a function to close the program
def exiting():
    # conformation message, do you really want to exit the program
	sure=messagebox.askyesno(title="Alert",message="Are you sure you want to exit?")
    # if the user clicks yes which means he/she wants to exit the program then the program is closed
	if sure==True:
		window.destroy()
    # if the user clicks no, the program won't exit
	else:
		return None
#Close
exitButton = Button(window,text = "EXIT")
exitButton.grid(row = 9, column = 2, columnspan = 6, pady = 7)
exitButton.configure(command = exiting,fg = "White" ,bg = "navy")

userNumbers = []
def userNumber():
    for i in range(0,6):
        lblEnter= Label(window, text="Press play before playing then enter 6 Numbers!")
        lblEnter.grid(row=0,column=1)
        entry1= StringVar()
        a= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey', textvariable=entry1,justify="center")
        a.grid(row = 1, column = 1, padx = 5, pady = 7)
        entry2= StringVar()
        b= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry2,justify="center")
        b.grid(row = 1, column = 2, padx = 5, pady = 7)
        entry3= StringVar()
        c= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry3,justify="center")
        c.grid(row = 1, column = 3, padx = 5, pady = 7)
        entry4= StringVar()
        d= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry4,justify="center")
        d.grid(row = 1, column = 4, padx = 5, pady = 7)
        entry5= StringVar()
        e= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry5,justify="center")
        e.grid(row = 1, column = 5, padx = 5, pady = 7)
        entry6= StringVar()
        f= Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='grey',textvariable=entry6,justify="center")
        f.grid(row = 1, column = 6, padx = 5, pady = 7)
        while (number in userNumbers):
            print("Duplicate, try again")
            number=("enter a unique number btwn 1 and 49")
        if (number>50 or number<1):
            print("Invalid Number, try again")
            number=("enter numb between 1 and 49")
        userNumbers.append(number)

def compare():
    # a = generatedNumbers()
    # b= userEntries()
    # result=[y for y in a if y in b]
    # print(result)


    counter=0
    for number in userNumbers:
        if number in lottoNumbers:
            counter +=1

    print("You guessed :", str(counter), "correctly")

#Comparison
compareButton = Button(window, width=20, text="Play", command=compare)
compareButton.configure(fg = "White" ,bg = "navy")
compareButton.grid(row = 9, column = 1, padx = 5, pady = 7)
#This is the line that runs the program until you exit
window.mainloop()
