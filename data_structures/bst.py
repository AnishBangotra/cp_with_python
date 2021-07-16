class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

class Tree:
	def createNode(self, data):
		return Node(data)

	def insert(self, node, data):
		if node is None:
			return self.createNode(data)
		if data < node.data:
			node.left = self.insert(node.left, data)
		elif data > node.data:
			node.right = self.insert(node.right, data)
		return node

	def search(self, node, data):
		if node is None or node.data == data:
			return node
		if node.data < data:
			return self.search(node.right, data)
		else:return self.search(node.left, data)

	def deleteNode(self, node, data):
		if node is None:
			return None
		if data < node.data:
			node.left = self.deleteNode(node.left, data)
		elif data > node.data:
			node.right = self.deleteNode(node.right, data)
		else:
			if node.left is None and node.right is None: del node
			if node.left == None:
				temp = node.right
				del node
				return temp
			elif node.right == None:
				temp = node.left
				del node
				return temp
		return node
		
	#-------DFS traverse in bfs ---------------
	def traverseInorder(self, root):
		if root is not None:
			self.traverseInorder(root.left)
			print(root.data)
			self.traverseInorder(root.right)

	def traversePreorder(self, root):
		if root is not None:
			print(root.data)
			self.traversePreorder(root.left)
			self.traversePreorder(root.right)

	def traversePostorder(self, root):
		if root is not None:
			self.traversePostorder(root.left)
			self.traversePostorder(root.right)
			print(root.data)


def main():
	root = None
	tree = Tree()
	root = tree.insert(root, 10)
	print(root)
	tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)

if __name__ == "__main__":
	main()

