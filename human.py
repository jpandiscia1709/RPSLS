# child class to player class
# 6.	Players choose their gestures
from player import Player

class Human(Player):
  def __init__(self):
      self.name = ''
      super().__init__()