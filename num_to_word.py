def number_to_words(number):
    # Define word representations for digits
    ones_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens_words = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens_words = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if number < 0 or number > 999:
        return "Number out of range, please enter a number between 0 and 999."

    if number == 0:
        return ones_words[number]

    words = []

    if number >= 100:
        words.append(ones_words[number // 100] + " hundred")
        number %= 100

    if number >= 20:
        words.append(tens_words[number // 10 - 1])
        number %= 10

    if 10 < number < 20:
        words.append(teens_words[number - 11])
        number = 0

    if number > 0:
        words.append(ones_words[number])

    return " ".join(words)


# Test the function
num = int(input('Enter the number'))
print(f"{num} in words is: {number_to_words(num)}")
