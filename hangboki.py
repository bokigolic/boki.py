from random import randrange

def chose_word_to_be_guessed():
    with open('C:\Bojan\_movies.txt', 'r') as words:
            word_list = [line[:1] for line in words.readlines()]
            index = randrange(len(word_list))
            
            return index

def get_letter_from_user():
    letter = str(input("Enter letter: "))
    while len(letter) !=1:
        letter = str(input("Try again: "))
    return letter

def print_list_or_underscores(word):
    temp_word_list = []
    for letter in word: 
        if letter == " ":
            temp_word_list.append(" ")
        else:
            temp_word_list.append("_")
    return temp_word_list

def convert_underscores_list_to_string(word_as_list):
    temp_word_string = ""
    for letter in word_as_list:
        temp_word_string = temp_word_string + letter
    return temp_word_string
   
def add_guessed_letter_to_underscore_list(user_letter, word, temp_word_list):
    for index, letter in enumerate(word):
        if user_letter == letter:
            temp_word_list.pop(index)
            temp_word_list.insert(index, letter)
        
    return temp_word_list

def offer_to_continue():
    choice = str(input("do you want to play again (y/n)"))
    while choice not in ("y", "n"):
        choice = str(input("Do you wanna play again? (y/n)"))
        if choice == "y":
            keep_playing = True
        elif choice == "n":
            keep_playing = False
        return keep_playing
        



def main():
    keep_playing = True
    while (keep_playing):
            word = chose_word_to_be_guessed()
            user_score = 3
            list_of_underscores = print_list_or_underscores(word)
            temp_word_string = convert_underscores_list_to_string(list_of_underscores)
            print(" ".join(temp_word_string))
           
            while user_score > 0:
                if temp_word_string == word:
                    print("Congraduation: ")
                    keep_playing = offer_to_continue()
            
            else:
                user_letter = get_letter_from_user()
            if user_letter in word:
                list_of_underscores = add_guessed_letter_to_underscore_list(user_letter, word, list_of_underscores)
            else:
                user_score = user_score -1
                if user_score == 0:
                        print(" ".join(temp_word_string.upper()))
                        print("your current score is: ", user_score)
                        keep_playing = offer_to_continue()
                        temp_word_string = convert_underscores_list_to_string(list_of_underscores)   
                        print("Sorry, you have no lives left! ")
                        print("Word you were unable to guess was: ", word)
    input("Press <Enter> to quit")        

    
    
main()