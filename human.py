# child class to player class
# 6.	Players choose their gestures
from player import Player

class Human(Player):


    class Human:
      def __init__(self, name):
        self.name = name
        super().__init__