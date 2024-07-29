


# list1=[]

# n=int(input("enter the range :") )
# for i in range(n):
#     i=input(str("enter element :"))
#     list1.append(i)

# print(list1)
# res=max(list1,key=len)
# print("Largest string is",res)
def custom_replace(str1, str2):
    # Create a dictionary to store the character counts in str1
    char_count = {}
    
    # Count the characters in str1
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Initialize the result string
    result = ""
    
    # Iterate through str2 and build the result string
    for char in str2:
        if char in char_count and char_count[char] > 0:
            result += char
            char_count[char] -= 1
    
    return result

# Test the function
str1 = "ABBBCC"
str2 = "XYZ"
result = custom_replace(str1, str2)
print(result)  # Output should be "ZXXXYY"

