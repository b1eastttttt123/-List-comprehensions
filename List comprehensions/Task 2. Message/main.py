# Creating an input
text = input("Enter the text: ")
add_symbol = input("Enter the additional character: ")

double_characters = [i * 2 for i in text] # for double symbol 
add_symbol_to_text = [i * 2 + add_symbol for i in text] # add symbol to text 

# Output
print("List of doubled characters:", double_characters)
print("Gluing with an additional symbol:", add_symbol_to_text)
