name=input("Enter your name: ")

a=[]
Vow=0
con=0
for i in name:
    if i.lower() in 'aeiou':
        Vow +=1
    else:
        con +=1

print(f"Total number of vowels is {Vow} and total number of consonants is {con}.")