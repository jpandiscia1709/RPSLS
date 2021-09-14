# child class to player
# 6.Players choose their gestures(random version

from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.name = "Braniac the Computer"
        print(self.name)
        super().__init__()
        
    def gesture_choice(self):
        self.chosen_gesture = random.choice(self.gesture)
        print("Braniac chooses:", self.chosen_gesture)


# for i in range (1):
    # print(random.choice(self_gesture))