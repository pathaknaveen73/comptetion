
def shape(n):
    row = n - 1
    for i in range(0, n):
        for j in range(0, row):
            print(end=" ")
        row = row - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")


n = int(input("Enter the number of rows :"))
shape(n)
