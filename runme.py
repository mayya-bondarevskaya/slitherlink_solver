 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from grid import Grid

clues = [[None, 3, 2, None, None, 3, None, None, 3, None, None, None, None, 2, 2],
		 [3, 1, None, None, None, None, 1, 3, 2, 2, None, 3, None, 3, None],
		 [None, None, 1, 1, None, 2, None, 1, 2, None, 3, None, 2, None, 1],
		 [2, 3, None, 2, None, None, None, None, None, 1, None, 1, None, None, 2],
		 [2, None, 2, None, None, 2, 2, None, None, None, 3, None, None, 2, None],
		 [3, None, None, 3, None, 3, 1, 2, None, 2, 2, None, 1, 2, None],
		 [None, None, None, 2, None, None, None, 0, None, None, None, None, None, None, None],
		 [None, None, None, None, 3, 1, 3, 2, None, None, 2, None, 1, None, 2],
		 [None, None, None, 2, None, None, 3, None, None, 3, None, 3, None, 3, None],
		 [None, 3, None, None, None, 1, None, None, None, 2, None, None, 1, 3, None],
		 [2, 3, None, 1, None, None, 2, None, 2, None, None, None, None, 2, 2],
		 [None, 2, 3, None, 1, None, 1, None, 1, None, None, 2, None, None, 2],
		 [None, 2, 2, 1, None, None, None, None, 3, None, None, None, 2, 1, None],
		 [None, 2, 3, None, 3, 1, None, 1, 2, None, None, 2, 2, 2, None],
		 [3, 2, 1, None, 2, 2, None, 3, 3, None, 2, 2, None, None, None]]

g = Grid(clues)
g.run(200)
g.print_grid()