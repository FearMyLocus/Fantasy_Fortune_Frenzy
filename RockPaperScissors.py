import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

options[0]
#Art
print('''
    ____             __      
   / __ \____  _____/ /__    
  / /_/ / __ \/ ___/ //_/    
 / _, _/ /_/ / /__/ ,<       
/_/ |_|\____/\___/_/|_|      
    ____                           
   / __ \____ _____  ___  _____    
  / /_/ / __ `/ __ \/ _ \/ ___/    
 / ____/ /_/ / /_/ /  __/ /        
/_/    \__,_/ .___/\___/_/         
           /_/                     
   _____      _                          
  / ___/_____(_)_____________  __________
  \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
 ___/ / /__/ (__  |__  ) /_/ / /  (__  ) 
/____/\___/_/____/____/\____/_/  /____/  
                                         

''')

while True:
    user_input = input("type rock/paper/scissors or Q to quit: ").lower()
    if user_input == ("q"):
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("TIE!")
        user_wins + 0

    elif user_input == "scissors" and computer_pick == "scissors":
        print("TIE!")
        user_wins + 0

    elif user_input == "rock" and computer_pick == "rock":
        print("TIE!")
        user_wins + 0

    else:
        print("you have lost!")
        computer_wins += 1
print("\nyou won", user_wins, "times.")
print("\nthe computer won", computer_wins, "times.")
print("thanks for playing... goodbye:) ")
time.sleep(0.5)
quit()