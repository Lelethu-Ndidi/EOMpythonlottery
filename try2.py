# #Creating a window
# from tkinter import *
import random
# from tkinter import messagebox
#
# #Creating a window
# window = Tk()
# window.title("6 Figure Lottery!!!")
# window.resizable(1000, 2000)
numbers = []
for num in ('1st', '2nd', '3rd', '4th', '5th', '6th'):
    while True:
        n = int(input('{} expected number: '.format(num)))
        if n not in range(1,50):
            print('Please enter a number from 1 to 49.')
        elif n in numbers:
            print('Duplicate numbers. Please re-enter.')
        else:
            numbers.append(n)
            break

*winners, additional_winner = random.sample(range(1,50), 7)
print("Lotto number for this week : {}, {}, {}, {}, {}, {}, and {}".format(*winners, additional_winner))
print("Your numbers are {}, {}, {}, {}, {}, {}".format(*numbers))

intersection = set(numbers) & set(winners)

if len(intersection) == 6:
    print("\nCongratulations! You are the 1st!")
elif len(intersection) == 5 and additional_winner in numbers:
    print("\nCongratulations! You are 2nd!")
elif len(intersection) == 5:
    print("\nCongratulations! You are 3rd!")
elif len(intersection) == 4:
    print("\nCongratulations! You are 4th!")
elif len(intersection) == 3:
    print("\nCongratulations! You are 5th!")
else:
   print("\nNext time...!")
# window.mainloop()
