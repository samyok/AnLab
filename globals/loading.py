from math import *


class Bar:
    def __init__(self):
        self.distance = 0
        self.text = "|>"
        for i in range(0, 20):
            self.text += " "
        self.text += " | [ ]"

    def update(self, fraction):
        # fraction is the fraction completed
        self.distance = floor(fraction * 20)
        self.text = "|"
        for i in range(0, self.distance):
            self.text += "="
        self.text += "=>"
        for i in range(self.distance, 20):
            self.text += " "
        self.text += "| [ ] "
        if self.distance >= 1:
            self.text = "|======================| [X] Done"
