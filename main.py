# #TextFile
#
# myfile = open("ithubaLotto.txt", "w")
# myfile.writelines("6 correct numbers: R10 000 000.00 \n")
# myfile.writelines("5 correct numbers: R8 584.00 \n")
# myfile.writelines("4 correct numbers: R2 384.00 \n")
# myfile.writelines("3 correct numbers: R100.50 \n")
# myfile.writelines("2 correct numbers: R20.00 \n")
# myfile.writelines("1 correct numbers: R0 \n")
# myfile.writelines("0 correct numbers: R0")
# myfile.close()
#
# #open and read the file after the appending:
# myfile = open("ithubaLotto.txt", "r")
# print(myfile.read())

import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,50)
  #Check if this number has already been picked and ...
  while number in lotteryNumbers:
    # ... if it has, pick a new number instead
    number = random.randint(1,50)

  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()


userNumbers = []
for i in range(0,6):
    number=int(input("Enter: "))
    while (number in userNumbers):
        print("Duplicate, try again")
        number=("enter a unique number btwn 1 and 49")
    if (number>50 or number<1):
        print("Invalid Number, try again")
        number=("enter numb between 1 and 49")
    userNumbers.append(number)

print("lotto num: ")
print(lotteryNumbers)

print("my guess:")
print(userNumbers)

counter=0
for number in userNumbers:
    if number in lotteryNumbers:
        counter +=1

print("You guessed :", str(counter), "correctly")
