#Creating a window
from tkinter import *
import random
from tkinter import messagebox

#Creating a window
window = Tk()
window.title("6 Figure Lottery!!!")
window.resizable(1000, 2000)
# messagebox.showinfo("\nPlease enter the 6 numbers you expected..")
enterNum= Label(window, text="Enter 6 Numbers!")
enterNum.grid(row=0,column=1)
def play():
    while True :
        entry= StringVar()
        a= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey', textvariable=entry)
        a.grid(row = 1, column = 1, padx = 5, pady = 7)
        a=int(a.get())
        if a == 0 :
            messagebox.showinfo("Error message","0 is less than 1. Please enter a number between 1 and 49")
            continue
        elif a < 50 :
            break
    messagebox.showinfo("Error message","Please enter a number from 1 to 49.")

    while True :
        b= StringVar()
        b= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey')
        b.grid(row = 1, column = 2, padx = 5, pady = 7)
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
        c= StringVar()
        c= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey')
        c.grid(row = 1, column = 3, padx = 5, pady = 7)
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
        d= StringVar()
        d= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey')
        d.grid(row = 1, column = 4, padx = 5, pady = 7)
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
        e= StringVar()
        e= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey')
        e.grid(row = 1, column = 5, padx = 5, pady = 7)
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
        f= StringVar()
        f= Entry(window, relief='groove', width = 5, bd=14, fg='white', bg='grey')
        f.grid(row = 1, column = 6, padx = 5, pady = 7)
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
            # messagebox.showinfo("--------------------------------------------------------")
            break
    messagebox.showinfo("Please enter a number from 1 to 49.")

    ## problematic part ##
    winners = random.sample(range(1,50), 7)
    messagebox.showinfo ("Error message","Lotto number for this week : {}, {}, {}, {}, {}, {}, and {}".format(*winners))
    messagebox.showinfo("The winning lotto numbers this week are", "%d, %d, %d, %d, %d, %d" %
    (a, b, c, d, e, f))

    if 'a, b, c, d, e, f' in winners :
        messagebox.showinfo("Error message","\nCongratulations! You are the 1st!")

    if ' "%d, %d, %d, %d, %d" % (a, b, c, d, e, f)' in winners :
        messagebox.showinfo("Error message","\nCongratulations! You are 2nd!")

    if ' "%d, %d, %d, %d" % (a, b, c, d, e, f)' in winners :
        messagebox.showinfo("Error message","\nCongratulations! You are 3rd!")

    if ' "%d, %d, %d" % (a, b, c, d, e, f)' in winners :
        messagebox.showinfo("Error message","\nCongratulations! You are 4th!")

    if ' "%d, %d" % (a, b, c, d, e, f)' in winners :
        messagebox.showinfo("Error message","\nCongratulations! You are 5th!")

    else :
       messagebox.showinfo("Error message","\nNext time...!")

def compare():
    pass
#Generate Numbers
compareButton = Button(window, width=20, text="Compare", command=compare)
compareButton.configure(fg = "White" ,bg = "navy")
compareButton.grid(row = 9, column = 1, padx = 5, pady = 7)
#This is the line that runs the program until you exit
window.mainloop()
