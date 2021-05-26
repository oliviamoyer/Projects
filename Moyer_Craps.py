# Olivia Moyer
# 001

# importing
import random

# running game 10 times
playerwins=0
dealerwins=0
for x in range (1,11):
    print("Playing Round:", x)

    # rolling the die for the first time
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print("Die 1:", die1, "Die 2:", die2)
    diesum=die1+die2

    # outcome of the roll
    if diesum==7 or diesum==11: 
        print("Player rolled:", diesum)
        print("Player wins!")
        playerwins+=1
    elif diesum==2 or diesum==3 or diesum==12:
        print("Player rolled:", diesum)
        print("Dealer wins.")
        dealerwins+=1
    else: 
        print("Points to match:", diesum, "...continue to roll!")
    # rolling until winner is confirmed
        while True: 
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            print("Die 1:", die1, "Die 2:", die2)
            rollforpoints=die1+die2
            print("Player now rolled:", rollforpoints)
            if rollforpoints==diesum:
                print("Player matched points of:", diesum,"...player wins!")
                playerwins+=1
                break
            elif rollforpoints==7:
                print("Player rolled:", rollforpoints, "...dealer wins.")
                dealerwins+=1
                break

print("Games Player Won: ", playerwins)
print("Games Dealer Won: ", dealerwins)