"""
Part - A:
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

Part - B:
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
"""

from pathlib import Path
from enum import Enum

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def from_letter(letter):
        if letter in ["A", "X"]:
            return Shape.ROCK
        if letter in ["B", "Y"]:
            return Shape.PAPER
        if letter in ["C", "Z"]:
            return Shape.SCISSORS

class Result(Enum):
    LOSE = "X"
    TIE = "Y"
    WIN = "Z"

SHAPE_TO_PICK = {
    Shape.ROCK: {
        Result.LOSE: Shape.SCISSORS,
        Result.WIN: Shape.PAPER,
    },
    Shape.PAPER: {
        Result.LOSE: Shape.ROCK,
        Result.WIN: Shape.SCISSORS,
    },
    Shape.SCISSORS: {
        Result.LOSE: Shape.PAPER,
        Result.WIN: Shape.ROCK,
    }
}

def score_for_game(moves):
    opp, me = moves

    # tie
    if me == opp:
        return me.value + 3

    # I win
    if (
        (me == Shape.ROCK and opp == Shape.SCISSORS)
        or (me == Shape.PAPER and opp == Shape.ROCK)
        or (me == Shape.SCISSORS and opp == Shape.PAPER)
    ):
        return me.value + 6

    # I lose
    return me.value

def parse_shape_and_result(game):
    shape, result = game.split(" ")
    return Shape.from_letter(shape), Result(result)

def value_for_game(moves):
    opp, me = moves

    # tie
    if me == opp:
        return me.value + 3

    # I win
    if (
        (me == Shape.ROCK and opp == Shape.SCISSORS)
        or (me == Shape.PAPER and opp == Shape.ROCK)
        or (me == Shape.SCISSORS and opp == Shape.PAPER)
    ):
        return me.value + 6

    # I lose
    return me.value

def value_for_desired_result(game_state):
    opp, res = game_state
    if res == Result.TIE:
        return value_for_game((opp, opp))

    return value_for_game((opp, SHAPE_TO_PICK[opp][res]))

if __name__ == "__main__":
    p = Path(__file__).with_name("day_two_input.txt")
    parse_shapes = tuple(map(Shape.from_letter, line.split(" ")) for line in open(p).read().splitlines())
    parse_goals = [parse_shape_and_result(line) for line in open(p).read().splitlines()]
    part_1 = sum(score_for_game(game) for game in parse_shapes)
    part_2 = sum(value_for_desired_result(state) for state in parse_goals)
    print(part_1) # ans = 13268
    print(part_2) # ans = 15508