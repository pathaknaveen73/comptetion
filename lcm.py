# import math


# print(math.lcm(45,36))
def hcf(g):
    x=2
    c=[]
    while g>1:
        if(g%x==0):
            g=g//x
            c.append(x)
        else:
            x+=1
    
    return c


            



a=int(input("enter the first number"))
list_a = hcf(a)
b=int(input("Enter the second number"))
list_b=hcf(b)
if list_b>list_a:
    for i in list_b:
        print(i)
else:
    for i in list_a:
         print(i)
