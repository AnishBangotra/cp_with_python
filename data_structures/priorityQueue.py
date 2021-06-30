#In Queue, the oldest element is dequeued first. While, in Priority Queue, element based on highest priority is dequeued.
#When elements are popped out of a priority queue then result obtained in either sorted in Increasing order or in Decreasing Order. While, when elements are popped from a simple queue, a FIFO order of data is obtained in the result.

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == 0

	def insert(self, data):
		self.queue.append(data)

	def delete(self):
		try:
			mx = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[mx]: mx = i
			val = self.queue[mx]
			del self.queue[mx]
			return val
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	queue = PriorityQueue()