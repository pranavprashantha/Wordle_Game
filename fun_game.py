####################
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignmenMrT."
#
# Name: Michael Urbina
#Saira Hussain
#Peter R
#pranav R 
# Section: 564
# Assignment: Lab: Topic 13 TEAM
# Date: 10 / 17 / 23
#
#

import random
import turtle as MrT


'''
Need to add More Detail ( 6 letter and capital)
Error in displaying letter matching


'''
########################################################P1
def Rule_Book():
    '''10 lines'''
    """Display the rules of the Wordle game with the details of the types of results with the entered input"""
    print("Welcome to off-brand Wordle!")
    print("Try to guess the secret word within 7 attempts for a 6 letter word.")
    print("After each guess, you'll receive feedback on your guess.")
    print("Feedback Legend:")
    print("  O: Correct letter and correct position")
    print("  X: Correct letter but wrong position")
    print("  -: Incorrect letter")

def User_StartUp():
    '''10 lines'''
    """Display a set of options for the player."""
    print("\nOptions:")
    print("1. Start Guessing the word!")
    print("2. Display instructions")
    print("3. Quit")
    
########################################################P2

import random
import turtle as MrT


'''
Need to add More Detail ( 6 letter and capital)
Error in displaying letter matching


'''
########################################################P1
def Rule_Book():
    '''10 lines'''
    """Display the rules of the Wordle game when prompted with addition of the of the types of values you can recieve based off your answer"""
    print("Welcome to off-brand Wordle!")
    print("Try to guess the secret word within 7 attempts.")
    print("After each guess, you'll receive feedback on your guess.")
    print("Feedback Legend:")
    print("  O: Correct letter and correct position")
    print("  X: Correct letter but wrong position")
    print("  -: Incorrect letter")

def User_StartUp():

    """Display a set of options for the player to guess in order for the user to get started with the game."""
    print("\nOptions:")
    print("1. Start Guessing the word!")
    print("2. Display instructions")
    print("3. Quit")
    
########################################################P2

def Word_Bank(): 
    '''10 lines'''
    """Pulling from Word Bank from opening the particular file and making sure they are 6 
    letters and randomly selecting in order to return a key with its value for future use"""
    # Update the file path to 'WorldFileEng.txt'
    #file_path = 'path/to/your/WorldFileEng.txt'

    # Read Word_50 from the file
    with open('WordleFileEng.txt', 'r') as WordBank:
        Word_Bank_50 = WordBank.read().splitlines()

    # Filter Word_Bank_50 with 6 letters
    word_6 = [word for word in Word_Bank_50 if len(word) == 6]

    # Choose a random word from the filtered list
    AKey = random.choice(word_6)
   # print(AKey)
    return AKey
########################################################P3
def display_feedback(AKey, guess): 
    '''10 lines'''
    """Display feedback on the player's guess base upon their results through appending the feedback from the 
    guess results."""
    feedback = []
    try: 
        for i in range((len(AKey))):
            if guess[i] == AKey[i].lower():
                feedback.append("O")
            elif guess[i] in AKey.lower():
                feedback.append("X")
            else:
                feedback.append("-")
        return " ".join(feedback)
    except:
        print("Your word must be 6 characters long")
    

def draw_smiley_face():
    '''just a simple print statement'''
    """Draw a simple smiley face."""


def circle():
    '''draws a circle'''

    MrT.penup()
    MrT.goto(0, -100)
    MrT.pendown()
    MrT.circle(100)

def eyes():
    '''draws eyes'''

    MrT.penup()
    MrT.goto(-40, 20)
    MrT.pendown()
    MrT.circle(10)
    MrT.penup()
    MrT.goto(40, 20)
    MrT.pendown()
    MrT.circle(10)

def mouth():

    '''draws mouth'''
    MrT.penup()
    MrT.goto(-40, -40)
    MrT.pendown()
    MrT.right(90)
    MrT.circle(40, 180)

def smiley_face():
    '''draws smiley face pulling all other functions'''
    t = MrT.Turtle()
    MrT.speed(2)
    circle()
    eyes()
    mouth()
    MrT.done()
    
########################################################P4

def Initiating_Game(count=0):
    """Play the Wordle game in which checks the amount of count iterations through adding to it with 
    an addition of printing whether or not you;ve satisifed or not in which you can."""
    AKey = Word_Bank()
    while count < 7:
        guess = input("\nEnter your guess: ").lower()
        if len(guess) > 6 or len(guess) < 6:
            print("Your word must be 6 characters long")
            print(f"Attempts left: {7 - count}")
        elif guess.lower() == AKey.lower():
            smiley_face()
        else:
            count += 1
            feedback = display_feedback(AKey, guess)
            print(f"Feedback:, {feedback}\nAttempts left: {7 - count}")
    if count == 7: print("\nSorry, you've run out of attempts. The secret word was:", AKey)
        
        
        

########################################################P1

# Main program
if __name__ == "__main__":
    Rule_Book()

    while True:
        User_StartUp()
        Selection_Choice = input("Enter your choice (1-3): ")

        if Selection_Choice == "1":
            Initiating_Game()
        elif Selection_Choice == "2":
            Rule_Book()
        elif Selection_Choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
