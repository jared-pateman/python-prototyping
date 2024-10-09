#!/usr/bin/python3
from enum import Enum


class Colours(Enum):
    YELLOW = 2
    GREEN = 3
    BROWN = 4
    BLUE = 5
    PINK = 6
    BLACK = 7


class ScoreHandler:
    def __init__(self):
        self.num_reds = 15
        self.is_on_red = True
        self.prev_num_reds = 15
        self.colours_remaining = [
            Colours.YELLOW,
            Colours.GREEN,
            Colours.BROWN,
            Colours.BLUE,
            Colours.PINK,
            Colours.BLACK
        ]
        self.current_break = 0
        self.last_pot = None

    @property
    def remaining_colour_value(self):
        colours_total = 0
        for colour_remaining in self.colours_remaining:
            colours_total += colour_remaining.value
        return colours_total

    @property
    def points_remaining(self):
        if self.is_on_red:
            return (8 * self.num_reds) + self.remaining_colour_value
        else:
            return ((8 * self.prev_num_reds) - 1) + self.remaining_colour_value

    @property
    def possible_break(self):
        return self.current_break + self.points_remaining

    def pot_red(self):
        self.prev_num_reds = self.num_reds
        self.num_reds -= 1
        self.current_break += 1
        self.last_pot = "red"
        self.is_on_red = False

    def pot_colour(self, colour):
        if self.prev_num_reds > 0 and self.last_pot == "red":
            self.current_break += colour.value
            self.last_pot = "colour"
            self.is_on_red = True
        else:
            self.prev_num_reds = 0
            self.current_break += colour.value
            self.colours_remaining.remove(colour)



score_handler = ScoreHandler()

print(
    "======== Start of Game ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

for i in range(15):
    score_handler.pot_red()

    print(
        "======== Red Potted! ========\n"
        f"Reds Remaining: {score_handler.num_reds}\n"
        f"Current Break: {score_handler.current_break}\n"
        f"Points Remaining: {score_handler.points_remaining}\n"
        f"Possible Break: {score_handler.possible_break}"
    )

    score_handler.pot_colour(Colours.BLACK)

    print(
        "======== Black Potted! ========\n"
        f"Reds Remaining: {score_handler.num_reds}\n"
        f"Current Break: {score_handler.current_break}\n"
        f"Points Remaining: {score_handler.points_remaining}\n"
        f"Possible Break: {score_handler.possible_break}"
    )

score_handler.pot_colour(Colours.YELLOW)
print(
    "======== Yellow Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

score_handler.pot_colour(Colours.GREEN)
print(
    "======== Green Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

score_handler.pot_colour(Colours.BROWN)
print(
    "======== Brown Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

score_handler.pot_colour(Colours.BLUE)
print(
    "======== Blue Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

score_handler.pot_colour(Colours.PINK)
print(
    "======== Pink Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)

score_handler.pot_colour(Colours.BLACK)
print(
    "======== Black Potted! ========\n"
    f"Reds Remaining: {score_handler.num_reds}\n"
    f"Current Break: {score_handler.current_break}\n"
    f"Points Remaining: {score_handler.points_remaining}\n"
    f"Possible Break: {score_handler.possible_break}"
)