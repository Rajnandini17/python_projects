import random
logo = '''
$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  
'''

print(logo)
print("WELCOME TO THE ROCK PAPER SCISSORS GAME!")
print("\n")

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

moves = [rock, paper, scissors]

def playgame():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You entered an invalid number!")
    else:
        print(moves[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"computer chose {computer_choice}")
        print(moves[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("User wins!")
        elif user_choice == 2 and computer_choice == 0:
            print("Computer wins!")
        elif user_choice < computer_choice:
            print("Computer wins!")
        elif user_choice > computer_choice:
            print("User wins!")
        elif user_choice == computer_choice:
            print("It's a draw.")

while True:
    playgame()
    if input("do you want to continue playing? type Y/N: ").lower() not in ["y", "yes"]:
        print("\n")
        print("THANKYOU FOR PLAYING")
        break



