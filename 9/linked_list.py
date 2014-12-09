class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

def insert_after(new_node, insert_at):
	new_node.next = insert_at.next
	insert_at.next = new_node

def remove_next(node):
	node.next = node.next.next

def length(node):
	if node.next == None:
		return 1
	else:
		return length(node.next) + 1

def print_list(node):
	if node.next == None:
		return str(node.value)
	else:
		return str(node.value) + ", " + print_list(node.next)

def print_list_iter(node):
	r = ""
	while node != None:
		r += str(node.value)
		r += ", "
		node = node.next
	return r[:-2]

def print_reverse_list(node):
	if node.next == None:
		return str(node.value)
	else:
		return  print_reverse_list(node.next) + ", " + str(node.value)

def insert(node, linked_list):
	if linked_list == None:
		return node
	elif node.value <= linked_list.value:
		node.next = linked_list
		return node
	else:
		linked_list.next = insert(node, linked_list.next)
		return linked_list

l = insert(Node(7), None)
l = insert(Node(6), l)
l = insert(Node(11), l)
l = insert(Node(12), l)
l = insert(Node(21), l)

print(print_reverse_list(l))
print(print_list_iter(l))
print(length(l))