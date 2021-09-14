# project start
from player import Player
from human import Human
from computer import Computer
from game import Game
   
# def __init__(self):
#        self.name = ''
#        self.gesture = ["rock", "paper", "scissors", "lizard", "spock" ]
# def set_name(self):
#        self.name = input("Enter player name:")
#        print("player name: ", self.name)
# def gesture_choice(self):
#        self.choice = print(self.gesture)
#        self.gesture_choice = input("Enter your gesture:")   

new_game = Game()
new_game.set_name()
new_game.game_type()
new_game.player_two.gesture_choice()

# def get_player_gestures(self):
#     self.player_one.gesture_choice()
#     self.player_two.gesture_choice()
#     compare_gestures()
