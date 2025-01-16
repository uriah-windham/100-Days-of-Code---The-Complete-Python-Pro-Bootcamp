import pandas

#TODO 1. Create a dictionary in this format:
phonetic_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in phonetic_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
letters = list(user_input)
code_words = [alphabet_dict[letter] for letter in letters]
print(code_words)