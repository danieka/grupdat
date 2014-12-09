class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

	def insert(self, node):
		if node.value <= self.value:
			node.next = self
			return node
		elif self.next == None:
			return node
		else:
			self.next = self.next.insert(node)
			return self

	def __len__(self):
		if self.next == None:
			return 1
		else:
			return len(node.next) + 1

	def __repr__(self):
		if self.next == None:
			return str(self.value)
		else:
			return str(self.value) + ", " + str(self.next)

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, value):
		node = Node(value)
		if self.head == None:
			self.head = node
		else:
			self.head.insert(node)


	def __len__(self):
		if self.head == None:
			return 0
		else:
			return len(self.head)
		
	def __repr__(self):
		return str(self.head)

l = LinkedList()
l.insert(7)
l.insert(13)
l.insert(3)
l.insert(15)

print(len(l))
print(l)