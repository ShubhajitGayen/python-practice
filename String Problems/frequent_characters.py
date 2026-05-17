word=input("Enter a word: ")
freq={}
for ch in word:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] =1

max_freq=max(freq.values())

print("Most frequent character(s): ")
for ch in freq:
        if freq[ch]==max_freq:
             print(ch,'->',freq[ch])

