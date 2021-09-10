# parent class to human class and computer class
# 6.	Players choose their gestures
class Player:
   def __init__(self):
       self.name = ''
       self.gesture = ["rock", "paper", "scissors", "lizard", "spock" ]
   def set_name(self):
       self.name = input("Enter player name:")
       print("player name: ", self.name)
   def gesture_choice(self):
       self.choice = print(self.gesture)
       self.gesture_choice = input("Enter your gesture:")   