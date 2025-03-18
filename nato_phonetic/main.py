import pandas as pd 

df = pd.read_csv("nato_phonetic/nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in df.iterrows()}
#print(nato_dic)




def generate_phonetic():
    user_input = input("Enter your word: ").upper()
    try:
        output_list = [nato_dic[letter] for letter in user_input]    
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
    
generate_phonetic()

# option 2 123
#word_list = []
#for character in user_input:
#    value = nato_dic.get(character.capitalize())
#    word_list.append(value)
#print(word_list)