#Ask the user to input a complete statement
statement_input = str(input("Please input a complete statement: "))

#Count how many words are in the statement
word_counter = len(statement_input.split()) #Use len.split() to count how many words

#Print the number of words
print("Word count: ", word_counter)