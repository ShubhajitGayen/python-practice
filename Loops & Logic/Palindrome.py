while True:
    try:
        number=int(input("Enter a number: "))
        break
    except:
        print("Only numbers are allowed.")


a=str(number)
b=[]
for i in a:
    b.append(i)

c=[]
for i in b[::-1]:
    c.append(i)

if b==c:
    print("It's a palindrome number.")
else:
    print("It's not a palindrome number.")
