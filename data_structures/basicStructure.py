class Node:
    def __init__(self, data=None):
        #we are creating data==None here so that when it came as last element it remains as
    	#None and before that on appending values in linked list we initalize it...
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()#initializing head with null Node

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = new_node

    def insertAtBeginning(self, value):
        if self.length == 0:
            new_node = Node(value)
            curr = self.head
            curr = new_node
        else:
            new_node = Node(value)
            curr = self.head
            new_node.next = curr
            curr = new_node


    def insert(self, pos, data):
        if pos<0 or pos>=self.length():
             print('Error: Index out of range!')
             return
        new_node = Node(data)
        curr = self.head
        curr_ind = 0
        while curr.next!=None:
            last_node = curr
            curr = curr.next
            if curr_ind == pos:
                last_node.next = new_node
                new_node.next = curr
                return
            curr_ind += 1

    def length(self):
        total = 0
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            total += 1
        return(total)

    def display(self):
        data = []
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            data.append(curr.data)
        print(data)

    def delete(self, index):
        if index < 0 or index >= self.length():
            print('Error: Index out of range!')
            return
        if index == 0:
            self.head = self.head.next
            return
        curr_ind = 0
        curr = self.head
        while True:
            last_node = curr
            curr = curr.next
            if curr_ind == index:
                last_node.next = curr.next
                return
            curr_ind += 1

    def inserting_values(self, data_list):
        for value in data_list:
            self.append(value)

    def removingDuplicates(self):
        marked = []
        curr = self.head
        marked.append(self.head.data)
        while curr.next!=None:
            last_node = curr
            curr = curr.next
            if curr.data not in marked:marked.append(curr.data)
            else:
                last_node.next = curr.next
                return

my_list = LinkedList()
my_list.append(3)
my_list.display()
my_list.append(45)
my_list.display()
my_list.inserting_values([3,4,7,9])
my_list.display()
print(my_list.length())
my_list.delete(1)
my_list.display()
my_list.insert(1,42)
my_list.display()
my_list.removingDuplicates()
my_list.display()
my_list.insertAtBeginning(5)
my_list.display()
