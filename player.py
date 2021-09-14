# parent class to human class and computer class
# 6.	Players choose their gestures
class Player:
   def __init__(self):
       self.name = ''
       self.gesture = ["rock", "paper", "scissors", "lizard", "spock" ]
       self.chosen_gesture = ''
       self.score = ''

   def set_name(self):
       self.set_name = input("Enter player 1 name:")
       self.player_one = ""
       self.player_two = ""  
       self.name = input("Enter player 2 name:")
       print("player one name: ", self.set_name)
       print("player two name: ", self.name)

   def gesture_choice(self):
       print("Please enter one of the following gestures: rock, paper, scissors, lizard, or spock")
       self.chosen_gesture = input("Enter your gesture:")   

