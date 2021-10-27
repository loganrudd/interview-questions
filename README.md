# interview-questions
Answers to a series of interview problems


## Synopsis

This repo attempts to solve the following problems from the 
code-questions-python.pdf file found in the root of this repo:

1. Math - Write a function that takes two integers (x and y) and returns a list
   of numbers between x and y that are divisible by 5 but not by 7

2. O.O. - Write a generator that takes a number N and returns all perfect 
   squares less than N. Hint: use yield
   Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially

3. Games - You have a chessboard with only the Rook on it. The Rook can move 
   up, down, left or right from your perspective. Write a function (or a class)
   that takes a series of movements and at the end of the sequence of movements 
   prints two numbers:
      a. The distance traveled by the Rook
      b. How far away the Rook is from its starting point
   Assume that the chessboard has no edges (the rook can travel any distance 
   in any direction). For example, if the Rook is moved in the following 
   sequence (up 1, left 3, down 2), then the Rook as traveled a distance of 6 
   spaces, and is 4 spaces away from its starting point.

4. File questions - Write a function that takes a phrase and a text file as 
   inputs. The function returns True if the phrase is found in the document and
   returns False otherwise. Note: Newline characters will not be included in 
   the phrase.

5. File questions - Give a Comma Separated File (csv) and a column number (zero
   being the left most column) return the sum of all the entries in that column
   Assume that all the entries in the CSV are numbers, and that there are no 
   column headers. 
   For example, if the file looks like this:
      1,2,3,4
      5,6,7,8
      9,10,11,12
   the sum of column 0 will be 1 + 5 + 9 = 15 and the sum of column 2 will be 
   3 + 7 + 11 = 21
`

## Instalation

Clone project, cd to root of directory, create a new virtual environment with 
python 3.9.6, activate, and install project with pip. Eg:

`conda create -n test python=3.9.6`

`conda activate test`

`pip install .`


## Code Example

Once virtual environment you can run the following 
commands to test the functionality the problems:

`$ python math_problem.py -x 25 -y 45`

`$ python oo_problem.py -n 25`

`$ python file_problem.py -p 'putant quaeque' -fp data/sample.txt`
`$ python file_problem_two.py -x 2 -fp data/sample.csv`

`$ python chess_twist.py -i 'u2, l1, r2, d3'`


## Tests

To run unit_tests for chess_game from root of directory simply run:

`python unit_tests/test_chess.py`
