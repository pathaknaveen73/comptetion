# Write a C program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.
unit=int(input("Enter the unit"))
if unit <= 50:
    totalunit=(50*0.50)
elif unit>50 and unit<=150:
    totalunit=(50*0.50) + (unit-50)*0.75
elif unit > 150 and unit<=250:
    totalunit=(50*0.50) + (100*0.75) + ((unit-150)*1.20)
elif unit>250:
    totalunit=(50*0.50) + (100*0.75) + (100*1.20) + ((unit-250)*1.50)
subcharge=(totalunit)*(20/100)
amount=totalunit+subcharge
print(amount)


