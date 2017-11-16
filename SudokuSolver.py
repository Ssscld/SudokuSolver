'''

Simple functional module to solve a 9x9 Sudoku puzzle. 
This module provides modules to read in a sudoku puzzle either from a website, a simple python gui or from a flat file
It also contains a solution engine to solve the puzzle. Included below is a sudoku explainer. 

The explainer content is from 

Package will provide
interface to interact with a web app (tbd)
interface to write to a file
interface for gui
standalone application

Input format (file or web)
-------------

r1 c1 n1
r2 c2 n2 
...

..where the first two numbers in each row eg 'r1 c1' refer to the row and column
number of the number 'n1' in the sudoku grid. Remember the grid is 0 indexed from the top left
(the top lefft corner cell has grid no (0 0), the cell to its right (0 1), the cell below so forth
 and so forth with eacch tuple being (r1 c1) Hence the r1 = actual row no -1 and similarly  for c1. 

The output file format will be ca 9x9 grid. Each row will have a comma separated list of solved 
grid column number and the file itself will have 9 rows. 

'''

INPUT_FILE = 'puzzles\\easy-1.txt'
OUTPUT_FILE='puzzles\\easu-1-solved.txt'


def main():
	with open (INPUT_FILE,'r') as f:
		for each in f: 
			print (each)


if __name__ == '__main__':
	main()
