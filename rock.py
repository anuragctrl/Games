import random
choice = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
computer_choice = random.choice(choice)
print(computer_choice)
if user_choice == computer_choice:
   print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
   (user_choice == "paper" and computer_choice == "rock") or \
   (user_choice == "scissors" and computer_choice == "paper"):
   print(" User win this round")
        
else:
   print("Computer wins this round")