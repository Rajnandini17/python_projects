import random
logo = '''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/             
'''

lives = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
print("WELCOME TO HANGMAN!")
print("\n")

word_list = ['ardvark', 'baboon', 'camel', 'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 
'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 
'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying']
choice = random.choice(word_list)

display = []
for letter in range(len(choice)):
    display += '_'
print(display)

end_of_game = False
hangman_lives = 6

while not end_of_game:
    user_choice = input("Guess a letter: ").lower()
    if user_choice in display:
        print(f"You've already guessed {user_choice}")
    for i in range(len(choice)):
        letter = choice[i]
        if letter == user_choice:
            display[i] = letter
    if user_choice not in choice:
        hangman_lives -= 1
        print("You lose a life, guess again.")
        print(lives[hangman_lives])

    print(display)

    if '_' not in display:
        end_of_game = True
        print("You Win!")
    if hangman_lives == 0:
        end_of_game = True
        print("You Lost!")
        print(f"The correct word is {choice}")

    
