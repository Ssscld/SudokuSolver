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

Setup: 
Script was developed in Python 3.4 but anything about python 3 will do. 
The command line version has 
SudokuSolver.py
a puzzles directory with files easy-1.txt and a generated file easy-1-solved.txt

filenames are hardcoded (for now, at least) as the needs for this script are to serve as a 
simple backend engine for a web-app. So I have a lot more else to worry about. But i kept it
structured enough to make it customizable in the future

Git Repo link: 


'''

INPUT_FILE = 'puzzles\\easy-1.txt'
OUTPUT_FILE='puzzles\\easy-1-solved.txt'

GRID_SIZE = 9 #Enable scalability to larger grids 

_mygrid = []

def initialize(grid = _mygrid):

	for i in range(GRID_SIZE): 
		grid.append([0 for _ in range (GRID_SIZE)])


def print_grid(grid=_mygrid, msg = ''): 
	_dashes = '-'*(len(msg)+3)+'\n' if len(msg) >21 else '_'*21+'\n'
	print(_dashes+msg+'\n'+_dashes)
	
	for i in range(GRID_SIZE):

		for j in range(GRID_SIZE): 
			print (grid[i][j], end = ' ')
			if (j+1)%3 == 0:
				print('  ', end = '')

		print()
	
		if (i+1)%3 == 0:
			print()
	print(_dashes+'\n')

def create_grid_from_file(grid = _mygrid):
	with open (INPUT_FILE,'r') as f:
		for each in f:
			nos =  list(map(int, each.split()))
			grid[nos[0]][nos[1]] = nos[2]

def write_grid_to_file(grid=_mygrid):
	with open (OUTPUT_FILE, 'w') as f:
		line = ''
		for i in range(GRID_SIZE):
			
			for j in range(GRID_SIZE): 
				line += str(grid[i][j]) + ' '
			
				if (j+1)%3 == 0:
					line += ' '

			line += '\n'
		
			if (i+1)%3 == 0:
				line += '\n'
		f.write(line)

def main():
	
	# initialize grid
	initialize()
	# print_grid()

	# read from file
	create_grid_from_file()
	print_grid(msg = 'after first creating grid')

	#write grid to file
	write_grid_to_file()

if __name__ == '__main__':
	main()
