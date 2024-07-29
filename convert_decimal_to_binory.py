a=[]
num=int(input("enter the decimal number"))

while num>=1:
    num1=num%2
    a.append(num1)
    num=num//2
print(a[::-1])

    


    




