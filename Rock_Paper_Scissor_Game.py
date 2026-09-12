# Rock Paper Scissor
import random
while True:
    comp_turn= random.choice(["Rock","Paper","Scissor"])
    user_turn= input("""Choose
                Rock
                Paper
                Scissor""").capitalize()
    print("Computer choose", comp_turn)
    print("You chose", user_turn)
    
    if user_turn == comp_turn:
        print("Tie")
    elif user_turn == "Scissor" and comp_turn == "Paper":
        print("You won")
        break
    elif user_turn == "Paper" and comp_turn == "Rock":
        print("You won")
        break
    elif user_turn == "Rock" and comp_turn== "Scissor":
        print("You won")
        break
    else:
        print("You lose")
