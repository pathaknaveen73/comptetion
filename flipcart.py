# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome(
#     'C:\\Users\\naveen.pathak\\Desktop\\Selenium2209\\chromedriver.exe')
# driver.get("https://www.flipkart.com/")
# driver.find_element(
# By.XPATH, '//input[@class="_3704LK"]').send_keys("Dove")

# time.sleep(1)
# driver.find_element(
#     By.XPATH, '//button[@class="L0Z3Pu"]').click()
# print("Searched Button Clicked")
# time.sleep(5)

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
