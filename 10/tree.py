class TreeNode:
	"""<Tree> ::= item <Tree> <Tree>"""
	def __init__(self,e):
		self.item
		self.left = None
		self.right = None

	def min(self):
		if self.left == None:
			return self.item
		else:
			self.left.min()

	def max(self):
		if self.right == None:
			return self.item
		else:
			self.right.max()

	def nodes(self):
		l = r = 0
		if self.right != None:
			r = self.right.nodes()
		if self.left != None:
			l = self.right.nodes()
		return r + l + 1

	def leaves(self):
		l = r = 0
		if self.right != None:
			r = self.right.leaves()
		if self.left != None:
			l = self.right.leaves()
		if l + r == 0:
			return 1
		else: 
			return r + l

class Tree:
	def __init__(self):
		self.root = None

	def min(self):
		self.root.min()

	def max(self):
		self.root.max()

	def nodes(self):
		self.root.nodes()

	def leaves(self):
		self.root.leaves()