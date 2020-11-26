from tkinter import *
from tkinter import messagebox

#creating a window
tkWindow = Tk()
#creating a window size
tkWindow.geometry('400x150')
#creating a window title
tkWindow.title('Play Lottery')

#username label and text entry box
name_lbl = Label(tkWindow, text="Name")
name_lbl.grid(row=0, column=0)
name_Entry = Entry(tkWindow)
name_Entry.grid(row=0, column=1)

#password label and password entry box
surname_lbl = Label(tkWindow,text="Surname")
surname_lbl.grid(row=1, column=0)
surname_Entry = Entry(tkWindow)
surname_Entry.grid(row=1, column=1)

def enter():
    name=name_Entry.get()
    surname=surname_Entry.get()
    if name or surname == "":
        messagebox.showinfo("Error message","Please enter your both your name and surname")
    else:
        return None

# Age label and Age Entry
age_lbl=Label(tkWindow,text="Age")
age_lbl.grid(row=2, column=0)
age_Entry = Entry(tkWindow)
age_Entry.grid(row=2, column=1)

#Function calculating the age
def Age():
    try:
        usersAge=int(age_Entry.get())
        if usersAge<18:
            raise ValueError(messagebox.showinfo("Error message","Sorry, you are too young to play"))
            tkWindow.destroy()
    except ValueError as e:
        print(e)
        age_Entry.delete(0,END)
        tkWindow.destroy()
    else:
        messagebox.showinfo("Login status","You can now start playing")
        tkWindow.withdraw()
        # Importing the play module so that when the age is greater than 18, the useer can now play the lottery
        import play
        play.playing()
        # if the user's age is less than 18, a message will be displayed which doesn't allow the user to play then the program will close.
#login button*
play_Button = Button(tkWindow, text="Play", command=Age)
play_Button.grid(row=4, column=0)

# Exit function
def exit_program():
    # conformation message, do you really want to exit the program
	sure=messagebox.askyesno(title="Alert",message="Are you sure you want to exit?")
    # if the user clicks yes which means he/she wants to exit the program then the program is closed
	if sure==True:
		tkWindow.destroy()
    # if the user clicks no, the program won't exit
	else:
		return None

# exit button
exitButton = Button(tkWindow, text="Exit", command=exit_program)
exitButton.grid(row=4, column=2)

tkWindow.mainloop()

# Now we need to do classes !
# And if num is not entered
# type error for surname and surname
