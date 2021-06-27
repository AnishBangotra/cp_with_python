class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)
		return self.stack

	def peek(self):
		print(self.stack[-1])
		return self.stack[-1]

	def pop(self):
		if len(self.stack) <= 0:return('No element present in stack')
		else:return self.stack.pop()

	def isEmpty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)

	def display(self):
		print(self.stack)
		
st = Stack()
