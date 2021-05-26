# Olivia Moyer
# 001

# import
import random

# function definitions
def equation(): 
    first=random.randint(0,12)
    second=random.randint(1,12)
    operator=random.randint(1,4)
    if operator==1:
        print(f'How much is {first} + {second}?')
        answer=first+second
        return answer
    elif operator==2:
        print(f'How much is {first} - {second}?')
        answer=first-second
        return answer
    elif operator==3:
        print(f'How much is {first} * {second}?')
        answer=first*second
        return answer
    else:
        both=first*second
        print(f'How much is {both} / {second}?')
        answer=(both)/(second)
        return answer

def accuracy(correct, total):
    try:
        score=(correct/total)*100
        return score
    except: 
        score="undetermined."
        return score

# calling functions and executing math test
correct=0
total=0
while True:
    # initiate or stop test
    practice=input("Type YES to practice or DONE to stop:",)
    if practice=="DONE":
        break
    elif practice=="YES":
        pass
    else: 
        print("Please enter either YES or DONE")
        continue
    # will print question and store answer in answer
    answer=equation()
    userin=input('Your answer:')
    try:
        userin=float(userin)
        # will continue if number was entered
        if answer==userin:
            print('Correct!')
            correct+=1
            total+=1
        else:
            print('Incorrect.')
            total+=1
    except:
            print('Incorrect, provide valid input next time.') 
            total+=1

score=accuracy(correct, total)
try:
    print(f'Your score is {score:^.2f}%')
except: 
    print(f'Your score is {score:^s}')
    

