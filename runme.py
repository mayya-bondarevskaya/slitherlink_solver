from grid import Grid

clues = [[None, 2, 2, None, 3],
		 [None, 2, None, None, None],
		 [3, 2, None, None, None],
		 [1, None, None, 0, 3],
		 [None, 2, 2, 3, None]]

g = Grid(clues)
g.print_grid()