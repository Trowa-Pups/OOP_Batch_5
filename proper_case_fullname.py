#Ask the user to input their fullname in incorrect casing
name_input = str(input("Please input your fullname in incorrect casing (Ex: TrOWa tANgcO): "))

#Print the input in proper casing
print(name_input.title()) #Use .title() to make it all first letters capitalized and the rest lowercase