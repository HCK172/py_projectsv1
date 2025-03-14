import pandas as pd 

df = pd.read_csv("nato_phonetic/nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in df.iterrows()}
#print(nato_dic)


user_input = input("Enter your name: ").upper()
output_list = [nato_dic[letter] for letter in user_input]
print(output_list) 

# option 2 
#word_list = []
#for character in user_input:
#    value = nato_dic.get(character.capitalize())
#    word_list.append(value)
#print(word_list)