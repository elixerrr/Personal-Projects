import random
import time
m=4
n = 0
block = ["1", "2", "3", "4", "5"]
print("Welcome to The Game!")
role = input("Which role do you want to play?(Hunter/Prey)")

while role == "Hunter" and n < 3:
    n += 1
    m=m-1 
    hider = random.choice(block)
    print("You will get a total of " + str(m) + " chances to catch the prey!") 
    time.sleep(0.5)
    print("Round " + str(n))
    time.sleep(0.5)
    print("Choose one of the blocks shown!")
    choice = input(str([f"|{b}|" for b in block]) + " Type the block number you want to attack in: ")
    if choice == hider:
        print("Congratulations you won! The block was |" + hider + "|")
        break
    else:
        print("Oops. The Hider was in the |" + hider + "| block.")
        time.sleep(1)
if role == "Prey":
    n = 0
    while n < 3:
        n += 1
        m=m-1
        hunter = random.choice(block)
        print("You will get a total of " + str(m) + " chances to hide from the hunter!")
        time.sleep(0.5)
        print("Round " + str(n))
        time.sleep(0.5)
        print("Choose one of the blocks shown!")
        choice = input(str([f"|{b}|" for b in block]) + " Type the block number you want to hide in: ")
        if choice == hunter:
            print("You lost :(. The hunter chose |" + hunter + "|")
            break
        else:
            print("You survived! The hunter chose |" + hunter + "|")
            time.sleep(1)
    else:
        print("You Win :)")
