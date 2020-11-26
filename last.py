#Creating a window
from tkinter import *
from random import sample
from tkinter import messagebox
import random


#Creating a window
window = Tk()
window.title("6 Figure Lottery!!!")
window.resizable(1000, 2000)

lottoNumbers = []

for i in range (0,6):
  number = random.randint(1,50)
  #Check if this number has already been picked and ...
  while number in lottoNumbers:
    # ... if it has, pick a new number instead
    number = random.randint(1,50)

  #Now that we have a unique number, let's append it to our list.
  lottoNumbers.append(number)

#Sort the list in ascending order
lottoNumbers.sort()

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


en1=int(a.get())
en2=int(b.get())
en3=int(c.get())
en4=int(d.get())
en5=int(e.get())
en6=int(f.get())
myLottoNumbers=[en1,en2,en3,en4,en5,en6]


myNumbers = []
def userNumbers():
    pass
    # while (number in myNumbers):
    #     messagebox.showinfo("Error message","No duplicate numbers allowed, Please try again")
    #     number=("Enter a unique number between 1 and 49")
    # if (number>50 or number<1):
    #     messagebox.showinfo("Error message","The entered number should be between 1 and 29, Please try again")
    #     number=("Enter a number between 1 and 49")
    # myNumbers.append(number)

def compare():
    print("Lottery number:\n ",lottoNumbers)
    # a = generatedNumbers()
    # b= userNumber()
    # result=[y for y in a if y in b]
    # print(result)

    # For textfile

    while (myLottoNumbers in myNumbers):
        messagebox.showinfo("Error message","No duplicate numbers allowed, Please try again")
        messagebox.showinfo("Message","Enter a unique number between 1 and 49")
    if (myLottoNumbers>50 or myLottoNumbers<1):
        messagebox.showinfo("Error message","The entered number should be between 1 and 29, Please try again")
        messagebox.showinfo("Message","Enter a number between 1 and 49")
    myNumbers.append(myLottoNumbers)
    counter=0
    for number in myNumbers:
        if number in lottoNumbers:
            counter +=1

    print("You guessed :", str(counter), "correctly")

compareButton = Button(window, width=20, text="Play", command=compare)
compareButton.configure(fg = "White" ,bg = "navy")
compareButton.grid(row = 9, column = 1, padx = 5, pady = 7)
#This is the line that runs the program until you exit
window.mainloop()
