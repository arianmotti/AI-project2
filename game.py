import random
import enum


class States(enum.Enum):
    state1 = 1
    state2 = 2
    state3 = 3


class Game:

    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0
        # addition
        first_pop_list = []
        first_pop_statelist = []

    # addition
    def first_pop(self, current_level_index, first_pop_list, first_pop_statelist):
        for i in range(200):
            first_pop_list[i] = random.randint(0, 2)
        first_pop_list[0] = 1
        first_pop_statelist[0] = enum.state1



    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_':
                steps += 1
            elif current_step == 'G' and actions[i - 1] == '1':
                steps += 1
            elif current_step == 'L' and actions[i - 1] == '2':
                steps += 1
            else:
                break
        return steps == self.current_level_len - 1, steps


g = Game(["____G__L__", "___G_M___L_"])
g.load_next_level()

# This outputs (False, 4)
print(g.get_score("0000000000"))
