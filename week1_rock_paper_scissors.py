# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# helper functions

def name_to_number(name):
    if name == "rock":
        return(0)
    elif name == "Spock":
        return(1)
    elif name == "paper":
        return(2)
    elif name == "lizard":
        return(3)
    elif name == "scissors":
        return(4)
    else:
        print("Error!")


def number_to_name(number):
    if number == 0:
        return("rock")
    elif number == 1:
        return("Spock")
    elif number == 2:
        return("paper")
    elif number == 3:
        return("lizard")
    elif number == 4:
        return("scissors")
    else:
        print("Error!")
    

def rpsls(player_choice): 
    # Part 1:
    # print a blank line to separate consecutive games
    # and print out the message for the player's choice
    print("\nPlayer chooses " + player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # Part 2:
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer chooses " + comp_choice)
    
    # Part 3:
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if diff in range(1,3):
        print("Computer wins!")
    elif diff in range(3,5):
        print("Player wins!")
    elif diff == 0:
        print("Player and computer tie!")
    else:
        print("Error!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
