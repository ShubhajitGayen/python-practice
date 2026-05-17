password = input("Enter the password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1


# Uppercase
for ch in password:
    if 'A' <= ch <= 'Z':
        score += 1
        break

# Lowercase
for ch in password:
    if 'a' <= ch <= 'z':
        score += 1
        break

# Number
for ch in password:
    if '0' <= ch <= '9':
        score += 1
        break

# Special character
special = '@#$%^&*'

for ch in password:
    if ch in special:
        score += 1
        break

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")