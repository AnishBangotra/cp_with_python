# You have a binary tree, finding inorder traversal of tree 
# without using recursion...

#Finding Inorder traversal using iterative approach(using stack)
class Node:
	def __init__(self, value):
		self.data = value
		self.left =  None
		self.right = None

def inOrder(self, root):
	res = []
	stack = []
	curr = root
	while True:
		if curr is not None:
			stack.append(curr)
			curr = curr.left
		elif stack:
			curr = stack.pop()
			print(curr.data, end=" ")
			curr = curr.right
		else:break
	print()

# Driver program for the program

root = Node(5)
root.right = Node(3)
root.left = Node(15)
root.left.left = Node(11)
root.left.right = Node(6)
inOrder(root)
