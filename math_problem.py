"""This module solves math problem number 1 from code-questions-python.pdf"""
import argparse


def five_but_not_seven(x, y):
    """Takes two integers (x and y) and returns a list of numbers between x and
    y that are divisible by 5 but not by 7
    :param x: (int) Starting number of range
    :param y: (int) Ending number of range
    :return: (list) Numbers between x and y that are divisiable by 5 but not 7

    >>> five_but_not_six(25, 45)
    [30, 40]
    """
    result = []
    for i in range(x + 1, y):
        if i % 5 == 0 and i % 7 !=0:
            result.append(i)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=int, required=True,
                        help='Starting range of numbers to be considered in '
                             'function five_but_not_seven.')
    parser.add_argument('-y', type=int, required=True,
                        help='Ending range of numbers to be considered in'
                             'function five_but_not_seven.')
    args = parser.parse_args()

    print(five_but_not_seven(args.x, args.y))
