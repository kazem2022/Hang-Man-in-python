#  HANG-MAN GAME
import random
from pathlib import Path

path1 = Path('random-words.txt')
words = path1.read_text()
words = words.split()
goal = random.choice(words)
goal = goal.lower()
goal_len = len(goal)


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def win():
    print("congratulation !!!!!!! you win")
 
    
def lost():
    print("ooooohhhh!!!  you losse  ")
    

print(f"------the answer has {goal_len} characters------")
goal_set = set(goal)

###ERROR HANDLING##########
alphabet = "abcdefghijklmnopqrstuvwxyz"
user_input_list = []
hang = 0
health = 6
word = "_"* goal_len
print("welcome to HANGMAN")

while health:
    #USER INPUT
    user_input = str(input("input a letter: ")).lower()           
    if user_input in alphabet: 
        if user_input in goal:
            for i, char in enumerate(goal):
                if user_input == char:
                    if user_input in user_input_list:
                        print("You have already entered this character")
                        continue
                    else:    
                        goal_set.remove(user_input)
                        user_input_list.append(char)
                        word = word[:i] + char + word[i+1:]
                        print(word)
                        print(user_input_list)
                      
                else:
                    print("_", end = "")
                
            print("\n.................................................................")
        
        else:
            health -= 1
            hang += 1
            print(HANGMANPICS[hang])
            print("health is: " ,health)
            if health == 0:         
                lost()
                break
            
    else:
        print("enter a valid letter A - Z:")
        continue
    
    
    if not goal_set:
        win()
        break
    