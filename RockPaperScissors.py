import random
test = True
question = "Yes"
i = 0 
q= 0
while question.lower() == "yes" or question.lower() == "y":
    choice2 = ["Rock", "Paper", "Scissors"]
    randochoice2= random.choice(choice2)
    random3 = "It's a draw!"
    random1 = "You win :)"
    random2 = "You lose :("
    phrase= "The opponent chose "
    if test == True:
        i = i + 1
    if test == False:
        q = q + 1
    else:
        i==i and q==q
    haha= str(i)
    haha2= str(q)
    haha3=  haha + "|" + haha2
    choice = input("What do you want to put out?(Rock/Paper/Scissors)")
    if choice.lower() == "rock" and randochoice2.lower() == "rock":
        print(phrase + randochoice2 + ". " + random3)
    if choice.lower() == "rock" and randochoice2.lower() == "paper":
        test= False        
        print(phrase + randochoice2 + ". " + random2)
    if choice.lower() == "rock" and randochoice2.lower() == "scissors":
        test= True
        print(phrase + randochoice2 + ". " + random1)
    if choice.lower() == "paper" and randochoice2.lower() == "paper":
        print(phrase + randochoice2 + ". " + random3)
    if choice.lower() == "paper" and randochoice2.lower() == "rock":
        test= True
        print(phrase + randochoice2 + ". " + random1)
    if choice.lower() == "paper" and randochoice2.lower() == "scissors":
        test= False
        print(phrase + randochoice2 + ". " + random2)
    if choice.lower() == "scissors" and randochoice2.lower() == "scissors":
        print(phrase + randochoice2 + ". " + random3)
    if choice.lower() == "scissors" and randochoice2.lower() == "rock":
        test= False
        print(phrase + randochoice2 + ". " + random2)
    if choice.lower() == "scissors" and randochoice2.lower() == "paper":
        test= True
        print(phrase + randochoice2 + ". " + random1)
    print("The current score is " + haha3)
    question= input("Do you wish to play more?(Yes/No)")
    if question.lower()=="No":
        print("Thanks for playing! " + "Your score is " + haha3)
        exit()

