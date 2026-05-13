a,b=0,1
n=int(input("How many number you want? "))
print(a)
print(b)
for _ in range(1,n-1):
    c=a+b
    print(c)
    a=b
    b=c
