#Ask the user to input their full name in incorrect casing
name_input = str(input("Please input your fullname in incorrect casing (Ex: TrOWa tANgcO): "))

#Print the input in snake casing
name_input = name_input.lower()
print(name_input.replace(" ", "_"))