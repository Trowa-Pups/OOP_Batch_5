#Ask the user to input their fullname in incorrect casing
name_input = str(input("Please input your fullname in incorrect casing (Ex: TrOWa tANgcO): "))

#Print the input in pascal casing
name_input = name_input.title()
print(name_input.replace(" ", ""))