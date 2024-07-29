
text = input("Enter the String")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in text:
    if i in vowels:
        text = text.replace(i, "")

print("Without Vowels =", text)