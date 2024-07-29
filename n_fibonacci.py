
num=int(input("Enter the range :"))
first=0                                         
second=1                                         
if num<=0:
    print("The series is",first)
else:
    print(first,second,end=" ")
    for i in range(2,num):
        next=first+second                           
        print(next,end=" ")
        first=second
        second=next
