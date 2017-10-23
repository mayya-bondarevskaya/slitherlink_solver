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

	def check_patterns(self):
		self.find_nearby_threes()
		self.find_diag_threes()
		self.find_diag_three_and_one()
		self.find_part_solved_two()

	def check_intersections(self):
		self.check_intersection_two_sides()
		self.check_intersection_three_sides()
		self.check_intersection_four_sides()

	def check_clues(self):
		self.corner_clues()
		self.find_zeros()
		self.find_ones()
		self.find_twos()
		self.find_threes()

	def run(self, number_of_iterations):
		for i in range(number_of_iterations):
			self.check_intersections()
			self.check_clues()
			self.check_patterns()

	def print_grid(self):
		dot ="." #u"\u2022"
		cross = "x"
		hbar = "_" #u"\u2015"
		vbar = "|" #u"\u007C"
		for i in range(self.width):
			print(dot, end="")
			for j in range(self.width):
				if self.grid[i][j].top is 0:
					print(" ", end="")
				elif self.grid[i][j].top is 1:
					print(hbar, end="")
				else:
					print(cross, end="")
				print(dot, end="")
			print("")

			if self.grid[i][0].left is 0:
				print(" ", end="")
			elif self.grid[i][0].left is 1:
				print(vbar, end="")
			else:
				print(cross, end="")
			for j in range(self.width):
				if self.grid[i][j].clue is not None:
					print(self.grid[i][j].clue, end="")
				else:
					print(" ", end="")
				if self.grid[i][j].right is 0:
					print(" ", end="")
				elif self.grid[i][j].right is 1:
					print(vbar, end="")
				else:
					print(cross, end="")
			print("")

		print(dot, end="")
		for j in range(self.width):
			if self.grid[self.width-1][j].bottom is 0:
				print(" ", end="")
			elif self.grid[self.width-1][j].bottom is 1:
				print(hbar, end="")
			else:
				print(cross, end="")
			print(dot, end="")
		print("")

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
			for j in range(self.width):
				if (self.grid[i][j].clue == 3) and (self.grid[i+1][j].clue == 3):
					self.shade_top(i, j)
					self.shade_bottom(i, j)
					self.shade_bottom(i+1, j)
					if j is not 0:
						self.cross_bottom(i, j-1)
					if j is not self.width-1:
						self.cross_bottom(i, j+1)
		for i in range(self.width):
			for j in range(self.width - 1):
				if (self.grid[i][j].clue == 3) and (self.grid[i][j+1].clue == 3):
					self.shade_left(i, j)
					self.shade_right(i, j)
					self.shade_right(i, j+1)
					if i is not 0:
						self.cross_right(i-1, j)
					if i is not self.width-1:
						self.cross_right(i+1, j)

	def check_intersection_three_sides(self):
		end_id = self.width-1
		for i in range(end_id):
			top = self.grid[i][0].left
			right = self.grid[i][0].bottom
			bottom = self.grid[i+1][0].left

			if (top == -1) and (bottom == -1):
				self.cross_bottom(i, 0)
			elif (top == -1) and (bottom == 1):
				self.shade_bottom(i, 0)
			elif (top == 1) and (bottom == -1):
				self.shade_bottom(i, 0)
			elif (top == 1) and (bottom == 1):
				self.cross_bottom(i, 0)

			if (top == -1) and (right == -1):
				self.cross_left(i+1, 0)
			elif (top == -1) and (right == 1):
				self.shade_left(i+1, 0)
			elif (top == 1) and (right == -1):
				self.shade_left(i+1, 0)
			elif (top == 1) and (right == 1):
				self.cross_left(i+1, 0)

			if (right == -1) and (bottom == -1):
				self.cross_left(i, 0)
			elif (right == -1) and (bottom == 1):
				self.shade_left(i, 0)
			elif (right == 1) and (bottom == -1):
				self.shade_left(i, 0)
			elif (right == 1) and (bottom == 1):
				self.cross_left(i, 0)

			left = self.grid[0][i].top
			bottom = self.grid[0][i].right
			right = self.grid[0][i+1].top

			if (left == -1) and (right == -1):
				self.cross_right(0, i)
			elif (left == -1) and (right == 1):
				self.shade_right(0, i)
			elif (left == 1) and (right == -1):
				self.shade_right(0, i)
			elif (left == 1) and (right == 1):
				self.cross_right(0, i)

			if (left == -1) and (bottom == -1):
				self.cross_top(0, i+1)
			elif (left == -1) and (bottom == 1):
				self.shade_top(0, i+1)
			elif (left == 1) and (bottom == -1):
				self.shade_top(0, i+1)
			elif (left == 1) and (bottom == 1):
				self.cross_top(0, i+1)

			if (bottom == -1) and (right == -1):
				self.cross_top(0, i)
			elif (bottom == -1) and (right == 1):
				self.shade_top(0, i)
			elif (bottom == 1) and (right == -1):
				self.shade_top(0, i)
			elif (bottom == 1) and (right == 1):
				self.cross_top(0, i)

			top = self.grid[i][end_id].right
			left = self.grid[i][end_id].bottom
			bottom = self.grid[i+1][end_id].right

			if (top == -1) and (left == -1):
				self.cross_right(i+1, end_id)
			elif (top == -1) and (left == 1):
				self.shade_right(i+1, end_id)
			elif (top == 1) and (left == -1):
				self.shade_right(i+1, end_id)
			elif (top == 1) and (left == 1):
				self.cross_right(i+1, end_id)

			if (top == -1) and (bottom == -1):
				self.cross_bottom(i, end_id)
			elif (top == -1) and (bottom == 1):
				self.shade_bottom(i, end_id)
			elif (top == 1) and (bottom == -1):
				self.shade_bottom(i, end_id)
			elif (top == 1) and (bottom == 1):
				self.cross_bottom(i, end_id)

			if (left == -1) and (bottom == -1):
				self.cross_right(i, end_id)
			elif (left == -1) and (bottom == 1):
				self.shade_right(i, end_id)
			elif (left == 1) and (bottom == -1):
				self.shade_right(i, end_id)
			elif (left == 1) and (bottom == 1):
				self.cross_right(i, end_id)

			left = self.grid[end_id][i].bottom
			top = self.grid[end_id][i].right
			right = self.grid[end_id][i+1].bottom

			if (left == -1) and (top == -1):
				self.cross_bottom(end_id, i+1)
			elif (left == -1) and (top == 1):
				self.shade_bottom(end_id, i+1)
			elif (left == 1) and (top == -1):
				self.shade_bottom(end_id, i+1)
			elif (left == 1) and (top == 1):
				self.cross_bottom(end_id, i+1)

			if (left == -1) and (right == -1):
				self.cross_right(end_id, i)
			elif (left == -1) and (right == 1):
				self.shade_right(end_id, i)
			elif (left == 1) and (right == -1):
				self.shade_right(end_id, i)
			elif (left == 1) and (right == 1):
				self.cross_right(end_id, i)

			if (top == -1) and (right == -1):
				self.cross_bottom(end_id, i)
			elif (top == -1) and (right == 1):
				self.shade_bottom(end_id, i)
			elif (top == 1) and (right == -1):
				self.shade_bottom(end_id, i)
			elif (top == 1) and (right == 1):
				self.cross_bottom(end_id, i)

	def check_intersection_two_sides(self):
		end_id = self.width-1
		right = self.grid[0][0].top
		bottom = self.grid[0][0].left
		if right == -1:
			self.cross_left(0, 0)
		elif right == 1:
			self.shade_left(0, 0)
		if bottom == -1:
			self.cross_top(0, 0)
		elif bottom == 1:
			self.shade_top(0, 0)

		left = self.grid[0][end_id].top
		bottom = self.grid[0][end_id].right
		if left == -1:
			self.cross_right(0, end_id)
		elif left == 1:
			self.shade_right(0, end_id)
		if bottom == -1:
			self.cross_top(0, end_id)
		elif bottom == 1:
			self.shade_top(0, end_id)

		top = self.grid[end_id][0].left
		right = self.grid[end_id][0].bottom
		if right == -1:
			self.cross_left(end_id, 0)
		elif right == 1:
			self.shade_left(end_id, 0)
		if top == -1:
			self.cross_bottom(end_id, 0)
		elif top == 1:
			self.shade_bottom(end_id, 0)

		top = self.grid[end_id][end_id].right
		left = self.grid[end_id][end_id].bottom
		if left == -1:
			self.cross_right(end_id, end_id)
		elif left == 1:
			self.shade_right(end_id, end_id)
		if top == -1:
			self.cross_bottom(end_id, end_id)
		elif top == 1:
			self.shade_bottom(end_id, end_id)

	def find_diag_three_and_one(self):
		for i in range(self.width-1):
			for j in range(self.width-1):
				square_11 = self.grid[i][j]
				square_12 = self.grid[i][j+1]
				square_21 = self.grid[i+1][j]
				square_22 = self.grid[i+1][j+1]

				if (square_11.clue is 3) and (square_22.clue is 1):
					if (square_11.left is 1) and (square_11.top is 1):
						self.cross_bottom(i+1, j+1)
						self.cross_right(i+1, j+1)
					elif (square_22.right is -1) and (square_22.bottom is -1):
						self.shade_left(i, j)
						self.shade_top(i, j)
				elif (square_12.clue is 3) and (square_21.clue is 1):
					if (square_12.top is 1) and (square_12.right is 1):
						self.cross_left(i+1, j)
						self.cross_bottom(i+1, j)
					elif (square_21.left is -1) and (square_21.bottom is -1):
						self.shade_top(i, j+1)
						self.shade_right(i, j+1)
				elif (square_22.clue is 3) and (square_11.clue is 1):
					if (square_22.right is 1) and (square_22.bottom is 1):
						self.cross_left(i, j)
						self.cross_top(i, j)
					elif (square_11.left is -1) and (square_11.top is -1):
						self.shade_right(i+1, j+1)
						self.shade_bottom(i+1, j+1)
				elif (square_21.clue is 3) and (square_12.clue is 1):
					if (square_21.left is 1) and (square_21.bottom is 1):
						self.cross_top(i, j+1)
						self.cross_right(i, j+1)
					elif (square_12.top is -1) and (square_12.right is -1):
						self.shade_left(i+1, j)
						self.shade_bottom(i+1, j)

	def find_part_solved_two(self):
		for i in range(self.width-1):
			for j in range(self.width-1):
				if self.grid[i][j].clue is 2:
					top = self.grid[i][j].top
					right = self.grid[i][j].right
					bottom = self.grid[i][j].bottom
					left = self.grid[i][j].left
					if (bottom, right) is (0, 0) and\
					   (left, top) is (-1, 1) or (1, -1):
						diag_square = self.grid[i+1][j+1]
						if diag_square.left is 1:
							self.cross_top(i+1, j+1)
						elif diag_square.left is -1:
							self.shade_top(i+1, j+1)
						if diag_square.top is 1:
							self.cross_left(i+1, j+1)
						elif diag_square.top is -1:
							self.shade_left(i+1, j+1)
					elif (bottom, left) is (0, 0) and\
						 (top, right) is (-1, 1) or (1, -1):
						diag_square = self.grid[i+1][j-1]
						if diag_square.top is 1:
							self.cross_right(i+1, j-1)
						elif diag_square.top is -1:
							self.shade_right(i+1, j-1)
						if diag_square.right is 1:
							self.cross_top(i+1, j-1)
						elif diag_square.right is -1:
							self.shade_right(i+1, j-1)
					elif (top, left) is (0, 0) and\
						 (bottom, right) is (-1, 1) or (1, -1):
						diag_square = self.grid[i-1][j-1]
						if diag_square.right is 1:
							self.cross_bottom(i-1, j-1)
						elif diag_square.right is -1:
							self.shade_bottom(i-1, j-1)
						if diag_square.bottom is 1:
							self.cross_right(i-1, j-1)
						elif diag_square.bottom is -1:
							self.shade_right(i-1, j-1)
					elif (top, right) is (0, 0) and\
						 (bottom, left) is (-1, 1) or (1, -1):
						diag_square = self.grid[i-1][j+1]
						if diag_square.left is 1:
							self.cross_bottom(i-1, j+1)
						elif diag_square.left is -1:
							self.shade_bottom(i-1, j+1)
						if diag_square.bottom is 1:
							self.cross_left(i-1, j+1)
						elif diag_square.bottom is -1:
							self.shade_bottom(i-1, j+1)

	def check_intersection_four_sides(self):
		for i in range(self.width-1):
			for j in range(self.width-1):
				top = self.grid[i][j].right
				right = self.grid[i][j+1].bottom
				bottom = self.grid[i+1][j+1].left
				left = self.grid[i+1][j].top
				if top is 1:
					if right is 1:
						self.cross_left(i+1, j+1)
						self.cross_top(i+1, j)
					elif bottom is 1:
						self.cross_bottom(i, j+1)
						self.cross_top(i+1, j)
					elif left is 1:
						self.cross_bottom(i, j+1)
						self.cross_left(i+1, j+1)
					elif right is -1:
						if bottom is -1:
							self.shade_top(i+1, j)
						elif left is -1:
							self.shade_left(i+1, j+1)
					elif (bottom is -1) and (left is -1):
						self.shade_bottom(i, j+1)
				elif right is 1:
					if bottom is 1:
						self.cross_top(i+1, j)
						self.cross_right(i, j)
					elif left is 1:
						self.cross_right(i, j)
						self.cross_left(i+1, j+1)
					elif bottom is -1:
						if left is -1:
							self.shade_right(i, j)
						elif top is -1:
							self.shade_top(i+1, j)
					elif (top is -1) and (left is -1):
						self.shade_left(i+1, j+1)
				elif bottom is 1:
					if left is 1:
						self.cross_right(i, j)
						self.cross_bottom(i, j+1)
					elif left is -1:
						if top is -1:
							self.shade_bottom(i, j+1)
						elif right is -1:
							self.shade_right(i, j)
					elif (right is -1) and (top is -1):
						self.shade_top(i+1, j)
				elif left is 1: 
					if top is -1:
						if right is -1:
							self.shade_left(i+1, j+1)
						elif bottom is -1:
							self.shade_bottom(i, j+1)
					elif (right is -1) and (bottom is -1):
						self.shade_right(i, j)

	def corner_clues(self):
		if self.grid[0][0].clue == 3:
			self.shade_left(0, 0)
			self.shade_top(0, 0)
		elif self.grid[0][0].clue == 2:
			self.shade_top(0, 1)
			self.shade_left(1, 0)
		elif self.grid[0][0].clue == 1:
			self.cross_left(0, 0)
			self.cross_top(0, 0)
		if self.grid[0][self.width-1].clue == 3:
			self.shade_right(0, self.width-1)
			self.shade_top(0, self.width-1)
		elif self.grid[0][self.width-1].clue == 2:
			self.shade_top(0, self.width-2)
			self.shade_right(1, self.width-1)
		elif self.grid[0][self.width-1].clue == 1:
			self.cross_right(0, self.width-1)
			self.cross_top(0, self.width-1)
		if self.grid[self.width-1][0].clue == 3:
			self.shade_left(self.width-1, 0)
			self.shade_bottom(self.width-1, 0)
		elif self.grid[self.width-1][0].clue == 2:
			self.shade_left(self.width-2, 0)
			self.shade_right(self.width-1, 1)
		elif self.grid[self.width-1][0].clue == 1:
			self.cross_left(self.width-1, 0)
			self.cross_bottom(self.width-1, 0)
		if self.grid[self.width-1][self.width-1].clue == 3:
			self.shade_right(self.width-1, self.width-1)
			self.shade_bottom(self.width-1, self.width-1)
		elif self.grid[self.width-1][self.width-1].clue == 2:
			self.shade_right(self.width-2, self.width-1)
			self.shade_bottom(self.width-1, self.width-2)
		elif self.grid[self.width-1][self.width-1].clue == 1:
			self.cross_right(self.width-1, self.width-1)
			self.cross_bottom(self.width-1, self.width-1)

	def find_zeros(self):
		for i in range(self.width):
			for j in range(self.width):
				if self.grid[i][j].clue == 0:
					self.cross_top(i, j)
					self.cross_bottom(i, j)
					self.cross_right(i, j)
					self.cross_left(i, j)

	def find_ones(self):
		for i in range(self.width):
			for j in range(self.width):
				if self.grid[i][j].clue == 1:
					top = self.grid[i][j].top
					right = self.grid[i][j].right
					bottom = self.grid[i][j].bottom
					left = self.grid[i][j].left
					if left == 1:
						self.cross_top(i, j)
						self.cross_right(i, j)
						self.cross_bottom(i, j)
					elif top == 1:
						self.cross_right(i, j)
						self.cross_bottom(i, j)
						self.cross_left(i, j)
					elif right == 1:
						self.cross_bottom(i, j)
						self.cross_left(i, j)
						self.cross_top(i, j)
					elif bottom == 1:
						self.cross_left(i, j)
						self.cross_top(i, j)
						self.cross_right(i, j)
					elif (left == -1) and (top == -1) and (right == -1):
						self.shade_bottom(i, j)
					elif (top == -1) and (right == -1) and (bottom == -1):
						self.shade_left(i, j)
					elif (right == -1) and (bottom == -1) and (left == -1):
						self.shade_top(i, j)
					elif (bottom == -1) and (left == -1) and (top == -1):
						self.shade_right(i, j)

	def find_threes(self):
		for i in range(self.width):
			for j in range(self.width):
				if self.grid[i][j].clue == 3:
					if (self.grid[i][j].top == -1):
						self.shade_right(i,j)
						self.shade_left(i,j)
						self.shade_bottom(i,j)
					elif (self.grid[i][j].bottom == -1):
						self.shade_right(i,j)
						self.shade_left(i,j)
						self.shade_top(i,j)
					elif (self.grid[i][j].right == -1):
						self.shade_left(i,j)
						self.shade_top(i,j)
						self.shade_bottom(i,j)
					elif (self.grid[i][j].left == -1):
						self.shade_right(i,j)
						self.shade_top(i,j)
						self.shade_bottom(i,j)

	def find_twos(self):
		for i in range(self.width):
			for j in range(self.width):
				if self.grid[i][j].clue == 2:
					top = self.grid[i][j].top
					right = self.grid[i][j].right
					bottom = self.grid[i][j].bottom
					left = self.grid[i][j].left
					if (top == -1) and (right == -1):
						self.shade_left(i,j)
						self.shade_bottom(i,j)
					elif (top == -1) and (bottom == -1):
						 self.shade_left(i,j)
						 self.shade_right(i,j)
					elif (top == -1) and (left == -1):
					     self.shade_right(i,j)
					     self.shade_bottom(i,j)
					elif (bottom == -1) and (left == -1):
					     self.shade_right(i,j)
					     self.shade_top(i,j)
					elif (bottom == -1) and (right == -1):
					     self.shade_top(i,j)
					     self.shade_left(i,j)
					elif (left == -1) and (right == -1):
					     self.shade_top(i,j)
					     self.shade_bottom(i,j)

					if (top == 1) and (right == 1):
						self.cross_left(i,j)
						self.cross_bottom(i,j)
					elif (top == 1) and (bottom == 1):
						 self.cross_left(i,j)
						 self.cross_right(i,j)
					elif (top == 1) and (left == 1):
					     self.cross_right(i,j)
					     self.cross_bottom(i,j)
					elif (bottom == 1) and (left == 1):
					     self.cross_right(i,j)
					     self.cross_top(i,j)
					elif (bottom == 1) and (right == 1):
					     self.cross_top(i,j)
					     self.cross_left(i,j)
					elif (left == 1) and (right == 1):
					     self.cross_top(i,j)
					     self.cross_bottom(i,j)

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