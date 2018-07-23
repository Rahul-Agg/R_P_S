import random
import os
import time

user_wins=0
computer_wins=0


#Instructions
print("""*************************************
Welcome to Rock Paper And Scissor...""")

user_name=input("Please enter your name. > ")

print("""*************************************
  WELCOME {} To this game

  The rules are simple:
  The computer and user choose from Rock,Paper,or Scissor.
  Rock crushes scissors.
  paper covers Rock.
  and
  Scissors cut paper

  you will play with computer...the first to reach 3 wins win the match.
  Good Luck!!
  ******************************************
  """.format(user_name))

while True:

    print("""
                    {} Wins:{}
                    computer wins:{}""".format(user_name,user_wins,computer_wins))

    user_choice=input("Please choose Rock(R),Paper(P),or Scissor(S): ").upper()

    #computer choice
    #1=rock
    #2=paper
    #3=Scissor

    random_number=random.randint(1,3)

    if random_number == 1:
        computer_choice = "R"

    elif random_number == 2:
        computer_choice = "P"

    elif random_number == 3:
        computer_choice = "S"

    if computer_choice == "R":
        print("""        
    ________
---'   _____) 
      (______)
      (______)
      (_____)
---.__(____)
    
The Computer chose rock. """)

    elif computer_choice == "P":
        print("""
__________________________
|-------------------------|
|-------------------------|
|-------------------------|
|-------------------------|
|-------------------------|
|-------------------------|
|-------------------------|                 
|-------------------------|                
|-------------------------|
|_________________________|
    
The Computer chose Paper.""")

    elif computer_choice == "S":
        print("""
    ________
---'    ____)____    
            _____) 
       ___________)      
       (_____)
---,___(____)
    
The Computer chose Scissor.""")


    #USER WINS
    #computer: R    user:P
    #computer: P    user:S
    #computer: S    user:R

    if (computer_choice == "R" and user_choice == "P" or
        computer_choice == "P" and user_choice == "S" or
        computer_choice == "S" and user_choice == "R"):
        print("{} Win!".format(user_name))
        user_wins+=1
    #COMPUTER WINS
    #computer:R     user:S
    #computer:P     user:R
    #computer:S     user:P

    elif (computer_choice == "R" and user_choice == "S" or
          computer_choice == "P" and user_choice == "R" or
          computer_choice == "S" and user_choice == "P"):
        print("{} Lose!".format(user_name))
        computer_wins+=1

    #TIE
    #computer:R     user:R
    #computer:P     user:P
    #computer:S     user:S

    elif (computer_choice == user_choice):
        print("Tie")

    if user_wins ==3:
        print("{} wins the match.".format(user_name))
        play_again=input("Would you like to play Again? (y/N) >")
        if play_again == 'Y':
            user_wins=0
            computer_wins=0
            continue
        else:
            exit()

    elif computer_wins ==3:
        print("Computer wins the match")
        play_again = input("Would you like to play Again? (y/N) >")
        if play_again == 'Y':
            user_wins=0
            computer_wins=0
            continue
        else:
            exit()

    if user_wins > computer_wins:
        print("{} looks confident!".format(user_name))
    elif user_wins < computer_wins:
        print("{} looks to be in a trouble!".format(user_name))
    else:
        print("Now both are equal(tie)")
