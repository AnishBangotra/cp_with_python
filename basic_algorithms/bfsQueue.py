#you can create either class of queue seperately with insert, pop and peek functions and use them 
#but lets take a look how to traverse by level through all the nodes of bst with the help of queue operations
#I'm using simple list as simple queue with same operations here!
#Algorithm we gonna use is=>
	#first we use while make it true and we already having a root value inside our queue
	#then pop it as queue works(FIFO) but we stored that value in a variable which gets pop
	#then search for its left and right which obviously gonna there if its a tree and append 
	#them to our queue and and also stored them in a string variable incrementing vise so that 
	#the pop element stored elemnt gets add into this string one by one as loop goes  and in the 
	#end we get our final list of all tree nodes data level order vise..

#traversing through by levels of BST
def level_Order(root):
	queue = []
	queue.append(root)
	traversed = ''
	while len(queue) > 0:
		node = queue.pop(0)
		if node.left:queue.append(node.left)
		if node.right:queue.append(node.right)
		traversed += str(node.data) + ' '
	return(traversed)
