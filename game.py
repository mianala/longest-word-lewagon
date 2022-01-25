import random
import string

class Game:

    def __init__(self):
        letters = string.ascii_uppercase
        self.grid =  list(''.join(random.choice(letters) for i in range(9)))

    def random_grid(self):
        letters = string.ascii_uppercase
        self.grid =  list(''.join(random.choice(letters) for i in range(9)))
        print(self.grid)

    def is_valid(self,word):
        if len(word) == 0 : return False
        for i in word:
            if i not in self.grid:
                return False
        return True