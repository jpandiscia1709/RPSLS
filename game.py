from player import Player
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
        player_one = ''
        player_two = '' 
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("Here are the rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
        
    def set_name(self):
        self.name = input("Enter player name:")
        print("player name: ", self.name)

    def run_game(self):
        # self.new_game = Game()
        self.new_game.game_type()
        self.new_game.player_one.set_name()
        self.new_game.player_one.gesture_choice()
        self.new_game.player_two.gesture_choice()
# player_one = ''
# player_two = ''

    def game_type(self):
        game_type = input("Please choose '1' for Single Player (Player vs. Computer) or '2' Multiplayer (Player 1 vs. Player 2)")
        if game_type == "1":
            self.player_one = Human()
            self.player_two = Computer()
        elif game_type == "2":
            self.player_one = Human()
            self.player_two = Human()
        else:
            print("Invalid Entry")

#    def gesture_choice(self):
#        print("Please enter one of the following gestures: rock, paper, scissors, lizard, or spock")
#        self.player_one.chosen_gesture = input("Enter your gesture:")  

# while True: 
#     game_type = input("Please choose '1' for Single Player (Player vs. Computer) or '2' Multiplayer (Player 1 vs. Player 2)")
#     if game_type == "1" or game_type == "2":
#         break
#     print("Invalid Entry")

#     player_one = Human()
# if game_type == "1":
#     player_two = Computer()
# else:
#     player_two = Human ()   
    # def run_game(self):
    
    #     self.welcome()
    #     self.choose_players()

    #     #game rounds


    #     #end game
    #     pass
0
    # def welcome(self):
    #     print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    #     print("Here are the rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
        
        
        
    # def choose_players(self):
    #     input("Please choose Single Player (Player vs. Computer) or Multiplayer (Player 1 vs. Player 2)")
     
    # def player_gesture(self):
    # Need to pull variable from self.chose_gesture
    #     player_gesture = 
    #     if player_gesture == gesture_choice
    #         print("Try Again")
    #         # run 'select a gesture'
    #     elif self.player_one.gesture == "rock" and self.player_two.gesture == "lizard" or "scissors":
    #         print("Player One Wins!")
    #         # add 1 to player one counter
    #     elif self.player_one.gesture == "paper" and self.player_two.gesture == "rock" or "spock":
    #         print("Player One Wins!")
    #     # add 1 to player one counter
    #     elif self.player_one == "scissors" and self.player_two == "lizard" or "paper":
    #         print("Player One Wins!")
    #     # add 1 to player one counter
    #     elif self.player_one.gesture == "lizard" and self.player_two.gesture == "paper" or "spock":
    #         print("Player One Wins!")
    #     # add 1 to player one counter
    #     elif self.player_one.gesture == "spock" and self.player_two.gesture == "rock" or "scissors":
    #         print("Player One Wins!")
    #     # add 1 to player one counter
    #     else:
    #         print("Player Two Wins!")
    #         # add 1 to player two counter

