import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, 'x':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence): 
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
   #success ltess goooo
    first_component = 0
    for letter in word:
      if letter != '*':
       first_component += SCRABBLE_LETTER_VALUES[letter.lower()] 
    second_component = (7 * len(word)) - (3 * (n-len(word)))
    if second_component < 1:
      second_component = 1
    score = first_component * second_component
    return score

# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    letter = random.choice(list(hand.keys()))
    if hand[letter] == 1:
         del hand[letter]
    else:
        hand[letter] -= 1
    hand.update({'*' : 1})
    
        

    
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    #lets gooo success
    new_hand = hand.copy() 
    for letter in word:
        letter = letter.lower()
        if letter in new_hand:
            if  new_hand[letter] > 1:
                new_hand[letter] = new_hand[letter] - 1
            else:
                del new_hand[letter]
    return new_hand
        


    pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    word = word.lower()
    temp_hand = hand.copy()
    if "*" in word:
        for vowel in VOWELS:
            if word.replace('*',vowel) in word_list: 
                word = word.replace('*',vowel)
                del temp_hand['*']
                temp_hand.update({vowel:1})
                print(word)
                break
    if word in word_list:
     for letter in word:
        letter = letter.lower()
        if letter in temp_hand:
            temp_hand[letter] = temp_hand[letter] - 1
            if temp_hand[letter] < 0:
                return False 
            else:
             pass 
        else:
            return False 
     return True
     
    else:
     return False

# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return len(hand)
    pass  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    total_score = 0
    while len(hand) != 0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        guess = input("Enter your guess: ")
        # If the input is two exclamation points:
        if guess == "!!" :
          break
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):
        else:
            if is_valid_word(guess,hand,word_list):
                total_score += get_word_score(guess,calculate_handlen(hand))
                print("Your score for this word is " + str(get_word_score(guess,calculate_handlen(hand))))
                print("Your total score is: " + str(total_score))
                hand = update_hand(hand,guess)
            # If the word is valid:
          
                # Tell the user how many points the word earned,
                # and the updated total score
            else:
              print("this word is not valid")
              hand = update_hand(hand,guess)
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            
    print( "your final score is: " + str(total_score))
    return total_score

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#
#I think this works as intended
def substitute_hand(hand, letter):
    temp_hand = hand.copy()
    if letter in temp_hand:
        if temp_hand[letter] == 1:
         del temp_hand[letter]
        else:
         temp_hand[letter] -= 1
        all_letters = string.ascii_lowercase
        for x in hand:
            all_letters = all_letters.replace(x,"")
        new_letter = random.choice(all_letters)
        temp_hand.update({new_letter : 1})
        return temp_hand


    else:
        print("that letter is not in hand \nplease enter a letter which is")
        return ""
    
       
    
def play_game(word_list):
    number_of_hands_left = int(input("How many number of hands would you like to play "))
    substitue = 1
    series_score = 0
    while int(number_of_hands_left) > 0:
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        
        if substitue != 0:
         x = input("would you like to subsitiute one letter from the hand (enter y or n) \n")
         if x == "y":
            letter = input("Which letter do you want to substitute\n")
            print("your new hand is \n")
            hand = substitute_hand(hand,letter)
            substitue -= 1
         elif x == "n":
            print("ok")
         else:
            print("invalid input")
        score = play_hand(hand,word_list)
        answer = input("Do you want to replay that hand (y/n)\n")
        if answer == "y":
            play_hand(hand,word_list)
            alt_score = play_hand(hand,word_list)
            if alt_score > score:
                score = alt_score
        series_score += score
        print("that hand is over")
        print("your series score is " + str(series_score))
        number_of_hands_left -= 1
    print ("The game is over You managed to score " + str(series_score))
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
