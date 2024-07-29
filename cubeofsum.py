def cubeofsum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    sum = 0
    for i in range(1, n+1) :
        sum = sum + pow(i ,3)
      
    return sum
  
# Driven Program
n = int(input("Enter the number"))
print(cubeofsum(n))