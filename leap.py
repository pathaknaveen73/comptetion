year=int(input("enter the year :"))
if year%400!=0 and year%100==0:
    print("this is not a leap year")
elif year%4!=0:
    print("this is not a leap year")
else:
    print("this is  leap year")
