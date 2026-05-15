word=input("Enter a word: ")
freq={}
for ch in word:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] =1

print("Duplicate charecture are: ")
for ch in freq:
    if freq[ch]>1:
        print(ch,'->',freq[ch])

