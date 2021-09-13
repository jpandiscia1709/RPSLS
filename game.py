from human import Human
from computer import Computer
class Game:
# 1.	A “friendly” welcome, and display the rules
# 2.	Choose single player (Human vs. AI) or multiplayer (Human vs. Human)
# 3.	Players enter names 
# 4.	How many rounds? (Remember that only three are required for the user story)
# 5.	Display the options for gestures
# 7.	Display the gestures that have been chosen
# 8.	Compare gestures
# 9.	Determine who won that round
# 10.	Track score (round wins) and check to see if someone has won the whole game (best of 3 minimum) (check every round)
# 11.	Display the winner
# 12.	 Do you want to play the entire game again?
    def __init__(self):
        self.welcome =  print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        self.rules = print("Here are the rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
        

    # def run_game(self):
    
    #     self.welcome()
    #     self.choose_players()

    #     #game rounds


    #     #end game
    #     pass

    # def welcome(self):
    #     print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    #     print("Here are the rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
        
        
        
    # def choose_players(self):
    #     input("Please choose Single Player (Player vs. Computer) or Multiplayer (Player 1 vs. Player 2)")
