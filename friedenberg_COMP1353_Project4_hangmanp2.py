"""
Author: Shane Friedenberg
Course: Data Structures and Algorithms I
Project: Malicious Hangman
FileName: friedenberg_COMP1353_Project4_hangmanp2.py
Date: 10/13/23
"""
from random import randint

        
def hangman():

    play_again = True
    #loop to allow for the player to play again if they choose
    while play_again is not False:
        #takes all of the words in a file and puts them into a dictionary
        with open('Dictionary.txt', 'r') as file:
            word_length = int(input("What word length do you want to choose? "))
            num_of_guesses = int(input("How many guesses do you want? ")) 
            words_at_length = []
            words = {}
            for i in range(word_length):
                for line in file:
                    line=line.strip().lower()
                    if len(line) == word_length:
                        words_at_length.append(line)
                words = {i+1 : words_at_length}


            #goes into the dictionary at the key of the chosen length and picks a random word from that list 
            for i in range(randint(0, len(words[word_length]))):
                word_to_guess = words[word_length][i]


        win = False
        set_of_guesses = set()
        user_answer = []
        #creates the user interface of the word that the user has to guess
        for i in range(len(word_to_guess)):
                user_answer.append("_")


        #loops until the user wins 
        while win == False:
            user_guess = input("Choose a letter to guess: ").lower()
            guessed = False
            

            #checks if the user inputed a letter that they have already guessed and if they haven't, add it to the list of guesses
            while guessed is not True:
                if user_guess in set_of_guesses:
                    user_guess = input(f"{user_guess} has already been guessed, guess another letter: ").lower()
                else:
                    set_of_guesses.add(user_guess)
                    break


            #checks if the users guess is in the answer and gives them the letters accordingly
            right_guess = False
            for i in range(len(word_to_guess)):
                if user_guess == word_to_guess[i]:
                    user_answer[i] = user_guess
                    right_guess = True
            if not right_guess:
                num_of_guesses -= 1
                print("Incorrect guess")
            else:
                print("Correct Guess!")
            print("number of guesses left: ", num_of_guesses)
            print(f"Used Letters: {set_of_guesses}")


            #tells the user that they are out of guesses and that they can try again with a different word
            if num_of_guesses == 0:
                print(f"Sorry but you are out of guesses. The word was {word_to_guess} Try again with another word.")
                break
            right_guess = False
            print(str(user_answer))


            #if the user guesses all the correct guesses before they run out of guesses, then they win! and they are asked if they want to play again
            if "_" not in user_answer:
                print("You Win!")
                print("Do you want to play again? ")
                replay = input("Type yes if you want to play again. Type anything else to quit. ").lower()
                if replay != "yes":
                    play_again = False
                win = True

def malicious_hangman():
    #loop to allow for the player to play again if they choose
    play_again = True
    #takes all of the words in a file and puts them into a set of remaining words
    while play_again is not False:
        with open('Dictionary.txt', 'r') as file:
            word_length = int(input("What word length do you want to choose? "))
            num_of_guesses = int(input("How many guesses do you want? ")) 
            remaining_words = set()
            set_of_guesses = set()
            guessed = False
            word_to_guess = ""
            for i in range(word_length):
                for line in file:
                    line=line.strip().lower()
                    if len(line) == word_length:
                        remaining_words.add(line)

            
            
            win = False
            just_swapped = True #this is so that if it doesn't say tha ta letter has been guessed already when it gets to the word that gets picked out

            #loops until the user wins
            while win == False:
                
                
                word_picked = False
                #this is where the user guesses and the words are removed until no words can be removed anymore and the word is picked
                while word_picked is False:
                    user_guess = input("Choose a letter to guess: ").lower()
                    #checks if the user inputed a letter that they have already guessed and if they haven't, add it to the list of guesses
                    while guessed is not True:
                        if user_guess in set_of_guesses:
                            user_guess = input(f"{user_guess} has already been guessed, guess another letter: ").lower()
                        else:
                            set_of_guesses.add(user_guess)
                            break

                    #uses the function select_new_word to cut out all of the necessary words until there are no more words to remove and then chooses a word a that point
                    set_of_guesses.add(user_guess)
                    remaining_words, word_to_guess = select_new_word(remaining_words, set_of_guesses, word_to_guess)
                    user_answer = []
                    for i in range(len(word_to_guess)):
                            user_answer.append("_")
                    for letter in set_of_guesses:
                        if letter in word_to_guess:
                            word_picked = True
                            break
                        
                    
                    num_of_guesses -= 1
                    if word_picked == False:
                        print(f"Guesses Remaining: {num_of_guesses}")
                        print("Incorrect guess")
                        print(user_answer)
                        print(set_of_guesses)


                #this is where the hangman actually starts with your remaining amount of guesses
                #checks if the user inputed a letter that they have already guessed and if they haven't, add it to the list of guesses
                while win is not True:
                    if just_swapped is False:
                        user_guess = input("Choose a letter to guess: ").lower()
                    while guessed is not True:
                        if user_guess in set_of_guesses and not just_swapped:
                            user_guess = input(f"{user_guess} has already been guessed, guess another letter: ").lower()
                        else:
                            just_swapped = False
                            set_of_guesses.add(user_guess)
                            break


                    right_guess = False
                    for i in range(len(user_answer)):
                        for letter in set_of_guesses:
                            if letter == word_to_guess[i]:
                                user_answer[i] = letter


                    #checks if the users guess is in the answer and gives them the letters accordingly
                    for letter in word_to_guess:
                        if letter == user_guess:
                            right_guess = True
                    if not right_guess:
                        num_of_guesses -= 1
                        print("Incorrect guess")
                    else:
                        print("Correct Guess!")
                    print("number of guesses left: ", num_of_guesses)
                    print(f"Used Letters: {set_of_guesses}")


                    #tells the user that they are out of guesses and that they can try again with a different word
                    if num_of_guesses == 0:
                        print(f"Sorry but you are out of guesses. The word was {word_to_guess} Try again with another word.")
                        break
                    right_guess = False
                    print(str(user_answer))


                    #if the user guesses all the correct guesses before they run out of guesses, then they win! and they are asked if they want to play again
                    if "_" not in user_answer:
                        print("You Win!")
                        print("Do you want to play again? ")
                        replay = input("Type yes if you want to play again. Type anything else to quit. ").lower()
                        if replay != "yes":
                            play_again = False
                        win = True
                    guessed = False    

            
def select_new_word(remaining_words, set_of_guesses, prev_word):

    #only add words that do not need to be removed based on what letters are in the set of guesses 
    updated_words = set()          
    for word in remaining_words:
        contains_letter = False
        for letter in set_of_guesses:
            if letter in word:
                contains_letter = True
        if not contains_letter:
            updated_words.add(word)


    #make the new word to guess one of the words from the list of words that has been updated from the words that have been removed 
    if len(updated_words) > 0:
        word_to_guess = updated_words.pop()


    #if every word in the list is removed, just set word to guess back to the previous word to guess    
    if len(updated_words) == 0:
        word_to_guess = prev_word
        
    #return a set of the new words and a new guess to store later
    return updated_words, word_to_guess
        
        


malicious_hangman()