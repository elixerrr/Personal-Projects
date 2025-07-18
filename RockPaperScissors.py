import random
i=0
q=0
question = "Yes"
while question.lower() == "yes" or question.lower() == "y":
    choice2 = ["Rock", "Paper", "Scissor"]
    move = random.choice(choice2)
    first = "It's a draw!"
    second = "You win :)"
    third = "You lose :("
    phrase= "The opponent chose "
    choice = input ("What do you want to put out?(Rock/Paper/Scissor)")
    if move== choice:
        print(first)
    if (choice== "Rock" and move=="Paper") or (choice== "Paper" and move=="Scissor") or (choice=="Scissor" and move=="Rock"):
        q= q+1
        player= str(i)
        computer= str(q)
        score= (player + "|" + computer)
        print(third+ phrase + move + "." + "The current score is " + score + ".")
    if (choice== "Paper" and move=="Rock") or (choice== "Scissor"and move=="Paper") or (choice=="Rock" and move=="Scissor"):
        i=i+1
        player= str(i)
        computer= str(q)
        score= (player + "|" + computer)
        print(second+ phrase + move + "." + "The current score is " + score + ".")    
    question= input("Do you wish to play more?(Yes/No)")
    if question.lower()== "no":
        print("Thanks for playing!")
        break

