
string=input("Enter the strings including digit and special char :")
alphabet=digit=spesial=0
for i in range(len(string)):
    if (string[i].isalpha()):
        alphabet=alphabet+1
    elif (string[i].isdigit()):
        digit=digit+1
    else:
        spesial=spesial+1
print(" total alphabet",alphabet)
print(" total digit",digit)
print(" total special char",spesial)

