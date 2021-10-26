"""This module solves O.O. problem number 1 from code-questions-python.pdf"""
import argparse


def perfect_squares_lt_n(n):
    """Generator that takes a number n and returns all perfect squares less
    than n

    :param n: (int) Upper limit of exclusive range of perfect squares to
        calculate
    :return: Generator object

    >>> perfect_square = perfect_squares_lt_n(16)
    >>> next(perfect_square)
    1
    >>> next(perfect_square)
    4
    >>> next(perfect_square)
    9
    >>> next(perfect_square)
    StopIteration
    """
    i = 1
    while i**2 < n:
        yield i**2
        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, required=True,
                        help='Upper limit of exclusive range of perfect '
                             'squares to return.')
    args = parser.parse_args()

    perfect_square = perfect_squares_lt_n(args.n)

    print('Generating all perfect squares less than {}'.format(args.n))
    while True:
        try:
            ps = next(perfect_square)
        except StopIteration:
            break
        print(ps)
