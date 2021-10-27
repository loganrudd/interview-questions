""" This module takes a very simple spin on the classic chess game with the
following criteria to solve problem 1 of Games in code-questions-python.pdf:

You have a chessboard with only the Rook on it. The Rook can move
   up, down, left or right from your perspective. Write a function (or a class)
   that takes a series of movements and at the end of the sequence of movements
   prints two numbers:
      a. The distance traveled by the Rook
      b. How far away the Rook is from its starting point
   Assume that the chessboard has no edges (the rook can travel any distance
   in any direction). For example, if the Rook is moved in the following
   sequence (up 1, left 3, down 2), then the Rook as traveled a distance of 6
   spaces, and is 4 spaces away from its starting point.
"""
from chess_game.utilities import main


class ChessGame:

    DIRECTION_DICT = {'l': 'x', }

    def __init__(self, origin={'x': 0, 'y': 0}):
        self.current_x = origin['x']
        self.current_y = origin['y']
        self.total_spaces_moved = 0
        self.spaces_from_start = 0

    def move_rook(self, direction, num_spaces):
        """
        Moves Rook num_spaces in given direction
        :param direction: (str) One letter character representing the direction
            to move in. l -> left, r -> right, d -> down, u -> up
        :param num_spaces: (int) Number of spaces to move
        :return:
        """
        if direction == 'l':
            self.current_x -= num_spaces
        elif direction == 'r':
            self.current_x += num_spaces
        elif direction == 'd':
            self.current_y -= num_spaces
        elif direction == 'u':
            self.current_y += num_spaces
        else:
            raise SyntaxError('Instruction set string not understood.'
                              'See move_series() docstring for proper syntax.')

    def move_series(self, instructions):
        """
        Takes a set of movement instructions to follow and prints the total
        number of spaces moved and number of spaces that the Rook is from it's
        last starting point.
        :param instructions: (str) Comma separated pair of alphanumeric
            characters with the first character being the direction to move in
            and the second character being the number of spaces to move in that
            direction, eg: 'u1,l2,d3,r4' would instruct the Rook to move up
            1 space, left 2 spaces, down 3 spaces, and right 4 spaces, in order
        :return: None
        """

        starting_x = self.current_x
        starting_y = self.current_y
        instructions_arr = instructions.split(',')
        for move in instructions_arr:
            move = move.strip()
            direction = move[0]
            number_of_spaces = int(move[1])
            self.total_spaces_moved += number_of_spaces
            self.move_rook(direction, number_of_spaces)
        self.spaces_from_start += \
            abs(starting_x - self.current_x) + abs(starting_y - self.current_y)
        print('Total spaces moved: {} \nSpaces from starting point: {}'.
              format(self.total_spaces_moved, self.spaces_from_start))


def start_game(args):
    """Reads command-line arguments and starts a game with those options."""
    import argparse
    parser = argparse.ArgumentParser(description="Play")
    parser.add_argument('-i', '--move_instructions', type=str,
                        help='A set of move instructions for the Rook to take.'
                             'See move_series docstring for proper format')
    args = parser.parse_args()

    chess_board = ChessGame()
    print('Rook initialized at origin ({},{})'.format(chess_board.current_x,
                                                      chess_board.current_y))
    chess_board.move_series(args.move_instructions)

@main
def run(*args):
    start_game(args)
