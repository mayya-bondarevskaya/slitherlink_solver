import numpy as np
from square import Square

class Grid(object):
	def __init__(self, clues):
		self.clues = clues
		self.width = len(clues)
		self.grid = []
		for i in range(self.width):
			temp_row = []
			for j in range(self.width):
				temp_row.append(Square(clues[i][j]))
			self.grid.append(temp_row)

	def find_diag_threes(self):
		for i in range(self.width - 1):
			if (self.grid[i][0].clue == 3) and (self.grid[i + 1][1].clue == 3):
				self.shade_left(i, 0)
				self.shade_top(i, 0)
				self.shade_right(i + 1, 1)
				self.shade_bottom(i + 1, 1)
			if (self.grid[i][self.width-1].clue == 3) and (self.grid[i+1][self.width-2].clue ==3):
				self.shade_right(i, self.width-1)
				self.shade_top(i, self.width-1)
				self.shade_bottom(i+1, self.width-2)
				self.shade_left(i+1, self.width-2)
			for j in range(1, self.width - 1):
				if (self.grid[i][j].clue == 3) and (self.grid[i+1][j+1].clue == 3):
					self.shade_left(i, j)
					self.shade_top(i, j)
					self.shade_right(i + 1, j + 1)
					self.shade_bottom(i + 1, j + 1)
				if (self.grid[i][j].clue == 3) and (self.grid[i+1][j-1].clue == 3):
					self.shade_top(i, j)
					self.shade_right(i, j)
					self.shade_left(i+1, j-1)
					self.shade_bottom(i+1, j-1)

	def find_nearby_threes(self):
		for i in range(self.width - 1):
			for j in range(self.width - 1):
				if self.grid[i][j].clue == 3:
					if self.grid[i][j + 1] == 3:
						self.shade_left(i, j)
						self.shade_right(i, j)
						self.shade_right(i, j + 1)
					if self.grid[i + 1][j] == 3:
						self.shade_top(i, j)
						self.shade_bottom(i, j)
						self.shade_bottom(i + 1, j)

	def shade_left(self, row, col):
		self.grid[row][col].shade_left()
		if col != 0:
			self.grid[row][col - 1].shade_right()

	def shade_right(self, row, col):
		self.grid[row][col].shade_right()
		if col != self.width - 1:
			self.grid[row][col + 1].shade_left()

	def shade_top(self, row, col):
		self.grid[row][col].shade_top()
		if row != 0:
			self.grid[row - 1][col].shade_bottom()

	def shade_bottom(self, row, col):
		self.grid[row][col].shade_bottom()
		if row != self.width - 1:
			self.grid[row + 1][col].shade_top()

	def cross_left(self, row, col):
		self.grid[row][col].cross_left()
		if col != 0:
			self.grid[row][col - 1].cross_right()

	def cross_right(self, row, col):
		self.grid[row][col].cross_right()
		if col != self.width - 1:
			self.grid[row][col + 1].cross_left()

	def cross_top(self, row, col):
		self.grid[row][col].cross_top()
		if row != 0:
			self.grid[row - 1][col].cross_bottom()

	def cross_bottom(self, row, col):
		self.grid[row][col].cross_bottom()
		if row != self.width - 1:
			self.grid[row + 1][col].cross_top()