# a = int(input("Enter the number"))
# s = sum([int(x)**len(str(a)) for x in str(a)])

# print(f'{a}=={s}')
# if a==s:
#     print('Yes, its armstrong number!')
# else:
#     print('No, its not armstrong number!')



num = int(input("enter the number"))
sum=0
while num%10!=0:
    reminder = num%10
    num=num//10
    num1=reminder**len(str(num))
    sum =  sum + num1
    print("loop---",num, reminder, num1, sum)

if num == sum:
    print('yes !',f'{num}=={sum}')

else:print('no')


