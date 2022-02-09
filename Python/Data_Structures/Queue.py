
class Queue():	
	def __init__( self ):
		self.items = [] 

	def is_empty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.append(item)

	def dequeue( self ):
		#FIFO 
		return self.items.pop( 0 )	
	
	def print_queue(self):
		return self.items

q = Queue()
print( q.is_empty())
q.enqueue("Homer")
q.enqueue("Marge")
q.enqueue("Bart")
q.enqueue("Lisa")
q.enqueue("Maggie")
print( q.print_queue())
q.dequeue()
print( q.print_queue())
print( q.is_empty())
