while True:
    try:
      number=int(input("Gave a Number: "))
      break
    except:
     print("Only number valid.")
if number<0:
   print("It's not a Armstrong number.")
else:
    a=str(number)
    b=len(a)

    l=[]
    for i in a:
        c=int(i)
        mul=c**b
        l.append(mul)

    if sum(l)==number:
        print("It's a Armstrong number.")
    else:
        print("It's not a Armstrong number.")
        