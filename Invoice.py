
original_str = "INV00989"
b=1
for i in range(b,b+100):
    str2 = "inv" + str(i)
    diff = len(original_str) - len(str2)
    zeros = diff*"0"
    new_str = "INV" + zeros + str(i)
    print(new_str)