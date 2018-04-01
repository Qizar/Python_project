import random

start = 0
computer_score = 0
human_score = 0

print("Welcome to rock paper scissors game")
print("You have got 3 chances\n")
name = input("Please enter your name: ")
print("\nPlease write 'r' for rock")
print("Please write 'p' for paper")
print("Please write 's' for scissors")


while start < 3:
    computer_choice = random.choice(['r','p','s'])
    human_choice = input("\nPlease read the above options and enter the value: ")
    if human_choice == 'r' and computer_choice == 'r':
        print("Draw !!!")
        print("Computer's choice",computer_choice)
    elif human_choice == 'r' and computer_choice == 'p':
        print("Computer wins !!!")
        computer_score = computer_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 'r' and computer_choice == 's':
        print(name,"wins !!!")
        human_score = human_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 'p' and computer_choice == 'r':
        print(name,"wins !!!")
        human_score = human_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 'p' and computer_choice == 'p':
        print("Draw !!!")
        print("Computer's choice",computer_choice)
    elif human_choice == 'p' and computer_choice == 's':
        print("Computer wins !!!!")
        computer_score = computer_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 's' and computer_choice == 'r':
        print("Computer wins !!!")
        computer_score = computer_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 's' and computer_choice == 'p':
        print(name,"wins !!!")
        human_score = human_score + 1
        print("Computer's choice",computer_choice)
    elif human_choice == 's' and computer_choice == 's':
        print("Draw !!!")
        print("Computer's choice",computer_choice)
    start = start + 1

if human_score > computer_score:
    print("\nOut of 3 rounds",name,'wins',human_score,'round(s)')
    print("Out of 3 rounds computer wins",computer_score,'round(s)')
    print("The winner of the game is",name)
elif human_score < computer_score:
    print("\nOut of 3 rounds computer wins",computer_score,'round(s)')
    print("Out of 3 rounds",name,'wins',human_score,'round(s)')
    print("The winner of the game is computer")
elif human_score == computer_score:
    print("\nNo one has won this game, Hahahahaha")
    print("\nOut of 3 rounds",name,'wins',human_score,'round(s)')
    print("Out of 3 rounds computer wins",computer_score,'round(s)')
