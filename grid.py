 #!/usr/bin/python
 # -*- coding: utf-8 -*-
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

	def print_grid(self):
		dot = u"\u2022"
		cross = "x"
		hbar = "_"#u"\u2015"
		vbar = "|"#u"\u007C"
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
		for i in range(self.width-1):
			if self.grid[i][0].left == -1:
				if self.grid[i+1][0].left == -1:
					self.cross_bottom(i, 0)
				elif self.grid[i+1][0].left == 1:
					self.shade_bottom(i, 0)
				elif self.grid[i][0].bottom == -1:
					self.cross_left(i+1, 0)
				elif self.grid[i][0].bottom == 1:
					self.shade_left(i+1, 0)
			elif self.grid[i][0].left == 1:
				if self.grid[i+1][0].left == 1:
					self.cross_bottom(i, 0)
				elif self.grid[i+1][0].left == -1:
					self.shade_bottom(i, 0)
				elif self.grid[i][0].bottom == 1:
					self.cross_left(i+1, 0)
				elif self.grid[i][0].bottom == -1:
					self.shade_left(i+1, 0)
			elif self.grid[i][0].bottom == -1:
				if self.grid[i+1][0].left == -1:
					self.cross_left(i, 0)
				elif self.grid[i+1][0].left == 1:
					self.shade_left(i, 0)
			elif self.grid[i][0].bottom == 1:
				if self.grid[i+1][0].left == 1:
					self.cross_left(i, 0)
				elif self.grid[i+1][0].left == -1:
					self.shade_left(i, 0)

			if self.grid[0][i].top == -1:
				if self.grid[0][i+1].top == -1:
					self.cross_right(0, i)
				elif self.grid[0][i+1].top == 1:
					self.shade_right(0, i)
				elif self.grid[0][i].right == -1:
					self.cross_top(0, i+1)
				elif self.grid[0][i].right == 1:
					self.shade_top(0, i+1)
			elif self.grid[0][i].top == 1:
				if self.grid[0][i+1].top == -1:
					self.shade_right(0, i)
				elif self.grid[0][i+1].top == 1:
					self.cross_right(0, i)
				elif self.grid[0][i].right == -1:
					self.shade_top(0, i+1)
				elif self.grid[0][i].right == 1:
					self.cross_top(0, i+1)
			elif self.grid[0][i].right == -1:
				if self.grid[0][i+1].top == -1:
					self.shade_top(0, i)
				elif self.grid[0][i+1].top == 1:
					self.cross_top(0, i)
			elif self.grid[0][i].right == 1:
				if self.grid[0][i+1].top == -1:
					self.shade_top(0, i)
				elif self.grid[0][i+1].top == 1:
					self.cross_top(0, i)

			if self.grid[i][self.width-1].right == -1:
				if self.grid[i+1][self.width-1].right == -1:
					self.cross_bottom(i, self.width-1)
				elif self.grid[i+1][self.width-1].right == 1:
					self.shade_bottom(i, self.width-1)
				elif self.grid[i][self.width-1].bottom == -1:
					self.cross_right(i+1,self.width-1)
				elif self.grid[i][self.width-1].bottom == 1:
					self.shade_right(i+1,self.width-1)
			elif self.grid[i][self.width-1].right == 1:
				if self.grid[i+1][self.width-1].right == -1:
					self.shade_bottom(i, self.width-1)
				elif self.grid[i+1][self.width-1].right == 1:
					self.cross_bottom(i, self.width-1)
				elif self.grid[i][self.width-1].bottom == -1:
					self.shade_right(i+1,self.width-1)
				elif self.grid[i][self.width-1].bottom == 1:
					self.cross_right(i+1,self.width-1)
			elif self.grid[i][self.width-1].bottom == -1:
				if self.grid[i+1][self.width-1].right == -1:
					self.cross_right(i, self.width-1)
				elif self.grid[i+1][self.width-1].right == 1:
					self.shade_right(i, self.width-1)
			elif self.grid[i][self.width-1].bottom == 1:
				if self.grid[i+1][self.width-1].right == -1:
					self.shade_right(i, self.width-1)
				elif self.grid[i+1][self.width-1].right == 1:
					self.cross_right(i, self.width-1)

			if self.grid[self.width-1][i].bottom == -1:
				if self.grid[self.width-1][i+1].bottom == -1:
					self.cross_right(self.width-1, i)
				elif self.grid[self.width-1][i+1].bottom == 1:
					self.shade_right(self.width-1, i)
				elif self.grid[self.width-1][i].right == -1:
					self.cross_bottom(self.width-1, i+1)
				elif self.grid[self.width-1][i].right == 1:
					self.shade_bottom(self.width-1, i+1)
			elif self.grid[self.width-1][i].bottom == 1:
				if self.grid[self.width-1][i+1].bottom == -1:
					self.shade_right(self.width-1, i)
				elif self.grid[self.width-1][i+1].bottom == 1:
					self.cross_right(self.width-1, i)
				elif self.grid[self.width-1][i].right == -1:
					self.shade_bottom(self.width-1, i+1)
				elif self.grid[self.width-1][i].right == 1:
					self.cross_bottom(self.width-1, i+1)
			elif self.grid[self.width-1][i].right == -1:
				if self.grid[self.width-1][i+1].bottom == -1:
					self.cross_bottom(self.width-1, i)
				elif self.grid[self.width-1][i+1].bottom == 1:
					self.shade_bottom(self.width-1, i)
			elif self.grid[self.width-1][i].right == 1:
				if self.grid[self.width-1][i+1].bottom == -1:
					self.shade_bottom(self.width-1, i)
				elif self.grid[self.width-1][i+1].bottom == 1:
					self.cross_bottom(self.width-1, i)

	def check_intersection_two_sides(self):
		if self.grid[0][0].top == -1:
			self.cross_left(0, 0)
		elif self.grid[0][0].left == -1:
			self.cross_top(0, 0)
		elif self.grid[0][0].top == 1:
			self.shade_left(0, 0)
		elif self.grid[0][0].left == 1:
			self.shade_top(0, 0)

		if self.grid[0][self.width-1].top == -1:
			self.cross_right(0, self.width-1)
		elif self.grid[0][self.width-1].right == -1:
			self.cross_top(0, self.width-1)
		elif self.grid[0][self.width-1].top == 1:
			self.shade_right(0, self.width-1)
		elif self.grid[0][self.width-1].right == 1:
			self.shade_top(0, self.width-1)

		if self.grid[self.width-1][0].bottom == -1:
			self.cross_left(self.width-1, 0)
		elif self.grid[self.width-1][0].left == -1:
			self.cross_bottom(self.width-1, 0)
		elif self.grid[self.width-1][0].bottom == 1:
			self.shade_left(self.width-1, 0)
		elif self.grid[self.width-1][0].left == 1:
			self.shade_bottom(self.width-1, 0)

		if self.grid[self.width-1][self.width-1].bottom == -1:
			self.cross_right(self.width-1, self.width-1)
		elif self.grid[self.width-1][self.width-1].right == -1:
			self.cross_bottom(self.width-1, self.width-1)
		elif self.grid[self.width-1][self.width-1].bottom == 1:
			self.shade_right(self.width-1, self.width-1)
		elif self.grid[self.width-1][self.width-1].right == 1:
			self.shade_bottom(self.width-1, self.width-1)

	def check_intersection_four_sides(self):
		for i in range(self.width-1):
			for j in range(self.width-1):
				if self.grid[i][j].right == -1:
					if self.grid[i][j+1].bottom == -1:
						if self.grid[i+1][j+1].left == -1:
							self.cross_top(i+1, j)
						elif self.grid[i+1][j+1].left == 1:
							self.shade_top(i+1, j)
					elif self.grid[i][j+1].bottom == 1:
						if self.grid[i+1][j+1].left == -1:
							self.shade_top(i+1, j)
						elif self.grid[i+1][j+1].left == 1:
							self.cross_top(i+1, j)
				elif self.grid[i][j].right == 0:
					if self.grid[i][j+1].bottom == -1:
						if self.grid[i+1][j+1].left == -1:
							if self.grid[i+1][j].top == 1:
								self.shade_right(i, j)
					elif self.grid[i][j+1].bottom == 0:
						if self.grid[i+1][j+1].left == 1:
							if self.grid[i+1][j].top == 1:
								self.shade_right(i, j)
								self.shade_bottom(i, j+1)
					elif self.grid[i][j+1].bottom == 1:
						if self.grid[i+1][j+1].left == -1:
							if self.grid[i+1][j].top == -1:
								self.shade_right(i, j)
						elif self.grid[i+1][j+1].left == 1:
							self.cross_right(i, j)
							self.cross_top(i+1, j)
				elif self.grid[i][j].right == 1:
					if self.grid[i][j+1].bottom == -1:
						if self.grid[i+1][j+1].left == -1:
							self.shade_top(i+1, j)
						elif self.grid[i+1][j+1].left == 0:
							if self.grid[i+1][j].top == 1:
								self.cross_left(i+1, j+1)
							elif self.grid[i+1][j].top == -1:
								self.shade_left(i+1, j+1)
						elif self.grid[i+1][j+1].left == 1:
							self.cross_top(i+1, j)
					elif self.grid[i][j+1].bottom == 0:
						if self.grid[i+1][j+1].left == -1:
							if self.grid[i+1][j].top == 1:
								self.cross_bottom(i, j+1)
							elif self.grid[i+1][j].top == -1:
								self.shade_bottom(i, j+1)
						elif self.grid[i+1][j+1].left == 0:
							if self.grid[i+1][j].top == 1:
								self.cross_bottom(i, j+1)
								self.cross_left(i+1, j+1)
						elif self.grid[i+1][j+1].left == 1:
							self.cross_bottom(i, j+1)
							self.cross_top(i+1, j)
					elif self.grid[i][j+1].bottom == 1:
						self.cross_left(i+1, j+1)
						self.cross_top(i+1, j)
				
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
					if (self.grid[i][j].top == -1) and\
					   (self.grid[i][j].right == -1):
						self.shade_left(i,j)
						self.shade_bottom(i,j)
					elif (self.grid[i][j].top == -1) and\
						 (self.grid[i][j].bottom == -1):
						 self.shade_left(i,j)
						 self.shade_right(i,j)
					elif (self.grid[i][j].top == -1) and\
					     (self.grid[i][j].left == -1):
					     self.shade_right(i,j)
					     self.shade_bottom(i,j)

					elif (self.grid[i][j].bottom == -1) and\
					     (self.grid[i][j].left == -1):
					     self.shade_right(i,j)
					     self.shade_top(i,j)
					elif (self.grid[i][j].bottom == -1) and\
					     (self.grid[i][j].right == -1):
					     self.shade_top(i,j)
					     self.shade_left(i,j)

					elif (self.grid[i][j].left == -1) and\
					     (self.grid[i][j].right == -1):
					     self.shade_top(i,j)
					     self.shade_bottom(i,j)

					elif (self.grid[i][j].top == 1) and\
					   (self.grid[i][j].right == 1):
						self.cross_left(i,j)
						self.cross_bottom(i,j)
					elif (self.grid[i][j].top == 1) and\
						 (self.grid[i][j].bottom == 1):
						 self.cross_left(i,j)
						 self.cross_right(i,j)
					elif (self.grid[i][j].top == 1) and\
					     (self.grid[i][j].left == 1):
					     self.cross_right(i,j)
					     self.cross_bottom(i,j)

					elif (self.grid[i][j].bottom == 1) and\
					     (self.grid[i][j].left == 1):
					     self.cross_right(i,j)
					     self.cross_top(i,j)
					elif (self.grid[i][j].bottom == 1) and\
					     (self.grid[i][j].right == 1):
					     self.cross_top(i,j)
					     self.cross_left(i,j)

					elif (self.grid[i][j].left == 1) and\
					     (self.grid[i][j].right == 1):
					     self.cross_top(i,j)
					     self.criss_bottom(i,j)

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