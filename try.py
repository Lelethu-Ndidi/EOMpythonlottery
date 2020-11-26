import random
## Variable declaration part ##
print("\nPlease enter the 6 numbers you expected..")
print("--------------------------------------------------------")

print("Please enter a number from 1 to 45.")
while True :
    a = int(input("1st expected number : "))
    if a == 0 :
        print("0 is the excluded number. Please re-enter.")
        continue
    elif a < 46 :
        break
print("Please enter a number from 1 to 45.")

while True :
    b = int(input("\2nd expected number : "))
    if b == 0 :
        print("0 is the excluded number. Please re-enter.")
        continue
    elif b == a :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif b < 46 :
        break
    print("Please enter a number from 1 to 45.")

while True :
    c = int(input("\n3rd expected number : "))
    if c == 0 :
        print("0 is the excluded number. Please re-enter.")
    elif c == a :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif c == b :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif c < 46 :
        break
    print("Please enter a number from 1 to 45.")

while True :
    d = int(input("\n4th expected number : "))
    if d == 0 :
        print("0 is the excluded number. Please re-enter.")
        continue
    elif d == a :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif d == b :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif d == c :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif d < 46 :
        break
    print("Please enter a number from 1 to 45.")

while True :
    e = int(input("\n5th expected number : "))
    if e == 0 :
        print("0 is the excluded number. Please re-enter.")
        continue
    elif e == a :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif e == b :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif e == c :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif e == d :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif e < 46 :
        break
    print("Please enter a number from 1 to 45.")

while True :
    f = int(input("\n6th expected number : "))
    if f == 0 :
        print("0 is the excluded number. Please re-enter.")
        continue
    elif f == a :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif f == b :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif f == c :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif f == d :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif f == e :
        print("Duplicate numbers. Please re-enter.")
        continue
    elif f < 46 :
        print("--------------------------------------------------------")
        break

## problematic part ##
winners = random.sample(range(1,41), 7)
print ("Lotto number for this week : {}, {}, {}, {}, {}, {}, and {}".format(*winners))
print("The lotto winning numbers are: ", "%d, %d, %d, %d, %d, %d" %
(a, b, c, d, e, f))

if 'a, b, c, d, e, f' in winners :
    print("\nCongratulations! You scored all 6 numbers and won R10 000 000")

elif ' "%d, %d, %d, %d, %d" % (a, b, c, d, e, f)' in winners :
    print("\nCongratulations! You scored all 5 numbers and won R8 584.00")

elif ' "%d, %d, %d, %d" % (a, b, c, d, e, f)' in winners :
    print("\nCongratulations! You scored all 4 numbers and won R2384.00")

elif ' "%d, %d, %d" % (a, b, c, d, e, f)' in winners :
    print("\nCongratulations! You scored all 3 numbers and won R100.50")

elif ' "%d, %d" % (a, b, c, d, e, f)' in winners :
    print("\nCongratulations! You scored all 2 numbers and won R20.00")
elif ' "%d" % (a, b, c, d, e, f)' in winners :
    print("\nYou scored 1, goodLuck for next time")
else :
   print("\nNext time...!")
