#Ask the user to input number from 0 - 1000
number_input = int(input("Please input a number from 0 - 1000: "))

#Print the number in six digit format and add zeros at the beginning to complete the format
print(str(number_input).zfill(6)) #Use str() to make the input into a string so that it can use .zfill(6) to add 0s