class Square(object):
	def __init__(self, clue = None):
		self.clue = clue
		self.top = 0
		self.bottom = 0
		self.left = 0
		self.right = 0

	def shade_top(self):
		self.top = 1
	def shade_bottom(self):
		self.bottom = 1
	def shade_right(self):
		self.right = 1
	def shade_left(self):
		self.left = 1