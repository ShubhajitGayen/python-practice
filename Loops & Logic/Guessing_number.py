import random

rand_num=random.randint(1,10)

while True:
    try:
        number = int(input("Enter a number in the range 1 to 10: "))
    except:
        print("Only numbers are allowed.")
    if 11>number>0:
        break
    else:
        print("Enter a valid number.")
   


if rand_num==number:
    print("You guessed the right number.")
else:
    print("Wrong guess.")
