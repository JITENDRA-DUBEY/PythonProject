# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
from replit import clear
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on=True
while is_on:

    word = input("Enter a word: ").upper()
    try:
      clear()
      output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print("sorry,only alphabet allowed in name other char not allowed")

    else:
      print(output_list)
      is_on=False
