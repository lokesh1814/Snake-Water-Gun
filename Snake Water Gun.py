#Snake Water Gun
"""Create a program using while loop or for loop and use random module. take input from user and also use random. If
the inut and random value mathecs show you won. The game willl continue till 10 times and then shows the score"""
"""Following are the rules of the game:

Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.

In situations where both players choose the same object, the result will be a draw."""


print("Welcome!! In the \"Snake Water Gun Game\"\n Choose any one out of Snake, Water and Gun\n")
rounds = 0
win = 0
lost = 0
draw = 0


while(True):

    print("Round> ", rounds)
    print("You won> ", win)
    print("You lost> ", lost)
    print("Draw between you and device> ", draw,"\n")
    print("This game will continue till 10 rounds")
    user = input("Enter Your Choice: ")
    lst = ["Snake", "Water", "Gun"]

    import random

    ran = random.choice(lst)

    if rounds >= 10:
        print(f"10 Rounds are over\nYou won {win} times.\n You Lost {lost} times.\n Draw between you and device {draw} times")
        print("Thanks for playing this game.")
        exit()

    if user == "Snake" and ran == "Snake":
        print("Its a Draw.\n")
        draw = draw + 1
        rounds = rounds + 1

    elif user == "Water" and ran == "Water":
        print("Its a Draw.\n")
        draw = draw + 1
        rounds = rounds + 1

    elif user == "Gun" and ran == "Gun":
        print("Its a Draw.\n")
        draw = draw + 1
        rounds = rounds + 1

    elif user == "Snake" and ran == "Water":
        print("WOW!!!\n Congrats, You won this round.\n")
        win = win + 1
        rounds = rounds + 1

    elif user == "Snake" and ran == "Gun":
        print("OOPS!!!\n Sorry, You lost this round.\n")
        lost = lost + 1
        rounds = rounds + 1

    elif user == "Water" and ran == "Snake":
        print("OOPS!!!\n Sorry, You lost this round.\n")
        lost = lost + 1
        rounds = rounds + 1

    elif user == "Water" and ran == "Gun":
        print("WOW!!!\n Congrats, You won this round.\n")
        win = win + 1
        rounds = rounds + 1

    elif user == "Gun" and ran == "Snake":
        print("WOW!!!\n Congrats, You won this round.\n")
        win = win + 1
        rounds = rounds + 1

    elif user == "Gun" and ran == "Water":
        print("OOPS!!!\n Sorry, You lost this round.\n")
        lost = lost + 1
        rounds = rounds + 1

    else:
        print("Error\n Check before you type.\n")
        break