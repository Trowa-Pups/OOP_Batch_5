#Ask the user to input their fullname with several space characters at the beginning
name_input = str(input("Please input your name with several spaces at the beginning: "))

#Print the input without the spaces in the beginning
print(name_input.strip()) #Using strip to remove the spaces