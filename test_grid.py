import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
	def test_shading(self):
		clues = [[None, None, None],
				 [None, None, None],
				 [None, None, None]]
		g = Grid(clues)
		g.shade_top(0,0)
		g.shade_right(1,1)
		g.shade_bottom(2,1)
		g.shade_left(0,2)
		self.assertEqual(g.grid[0][0].top, 1)
		self.assertEqual(g.grid[1][1].right, 1)
		self.assertEqual(g.grid[1][2].left, 1)
		self.assertEqual(g.grid[2][1].bottom, 1)
		self.assertEqual(g.grid[0][2].left, 1)
		self.assertEqual(g.grid[0][1].right, 1)

	def test_crossing(self):
		clues = [[None, None, None],
				 [None, None, None],
				 [None, None, None]]
		g = Grid(clues)
		g.cross_top(0,0)
		g.cross_right(1,1)
		g.cross_bottom(2,1)
		g.cross_left(0,2)
		self.assertEqual(g.grid[0][0].top, -1)
		self.assertEqual(g.grid[1][1].right, -1)
		self.assertEqual(g.grid[1][2].left, -1)
		self.assertEqual(g.grid[2][1].bottom, -1)
		self.assertEqual(g.grid[0][2].left, -1)
		self.assertEqual(g.grid[0][1].right, -1)

	def test_find_twos(self):
		clues = [[None, 2, None],
				 [None, None, None],
				 [None, 2, None]]
		g = Grid(clues)
		g.shade_left(0, 1)
		g.shade_top(0, 1)
		g.cross_bottom(2, 1)
		g.cross_right(2, 1)
		g.find_twos()
		self.assertEqual(g.grid[0][1].right, -1)
		self.assertEqual(g.grid[0][1].bottom, -1)
		self.assertEqual(g.grid[2][1].left, 1)
		self.assertEqual(g.grid[2][1].top, 1)

	def test_find_part_solved_two(self):
		clues = [[None, None, None, None],
				 [None, None, 2, None],
				 [None, None, None, None],
				 [None, None, None, None]]
		g = Grid(clues)
		g.shade_top(1, 2)
		g.cross_right(1, 2)
		g.shade_right(2, 1)
		g.find_part_solved_two()
		self.assertEqual(g.grid[2][1].top, -1)
		self.assertEqual(g.grid[2][1].right, 1)

if __name__ == '__main__':
	unittest.main()