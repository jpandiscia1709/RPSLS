# parent class to human class and computer class
# 6.	Players choose their gestures
class Player:
   def __init__(self):
       self.name = ''
       self.gesture = ["rock", "paper", "scissors", "lizard", "spock" ]
       self.chosen_gesture = ''

   def set_name(self):
       self.name = input("Enter player name:")
       print("player name: ", self.name)

   def gesture_choice(self):
       print("Please enter one of the following gestures: rock, paper, scissors, lizard, or spock")
       self.chosen_gesture = input("Enter your gesture:")   

