
class SingleLinkListNode: 
	def __init__( self, item ): 
		self.item  = item 
		self.next = None


class SingleLinkList: 
	def __init__( self):
		self.head = None 
		self.lenght = 0 

	def prepend( self, item ): 
		if self.head is None: 
			self.head = SingleLinkListNode( item )
		else: 
			newNode = SingleLinkListNode( item )
			newNode.next = self.head 
			self.head = newNode
		self.lenght += 1 

	def append( self, item ): 
		if self.head is None: 
			self.head = SingleLinkListNode( item )
		else: 
			newNode = SingleLinkListNode( item )			
			curNode = self.head 

			while curNode.next:				
				curNode = curNode.next
			curNode.next = newNode
		self.lenght += 1 

	def insert_after( self, item, prevNode):
		if self.head is None: 
			self.head = SingleLinkListNode( item )
		else:
			newNode = SingleLinkListNode( item )			
			curNode = self.head
			while curNode and curNode.item != prevNode: 			
				curNode = curNode.next
			if curNode: 
				newNode.next = curNode.next
				curNode.next = newNode
		self.lenght += 1 
				
	def traverse( self): 
		if self.head is None: 
			return 
		else: 
			self._traverse( self.head ) 
	
	def _traverse( self, curNode): 
		SingleLinkList_ = ""
		while curNode: 
			SingleLinkList_ += curNode.item	+ "--> "		
			curNode = curNode.next 
		print( SingleLinkList_ , end="")

	def remove( self, item ):
		if self.head.item == item: 
			self.head = self.head.next
		else: 
			prevNode = None
			curNode = self.head
			while curNode and curNode.item != item: 
				prevNode = curNode
				curNode = curNode.next 
			if curNode: 
				prevNode.next = curNode.next 			
				curNode = None 
		self.lenght -= 1 

	def swapNodes( self, node1, node2): 
		if node1 == node2 or self.head is None: 
			return 
		else: 
			prevNode1 = None 
			curNode1 = self.head
			while curNode1 and curNode1.item != node1: 
				prevNode1 = curNode1
				curNode1 = curNode1.next 

			prevNode2 = None 
			curNode2 = self.head
			while curNode2 and curNode2.item != node2: 
				prevNode2 = curNode2
				curNode2 = curNode2.next 

			if not curNode1 or not curNode2: 
				return 

			if prevNode1:
				prevNode1.next = curNode2
			else: 
				self.head = curNode2

			if prevNode2: 
				prevNode2.next = curNode1
			else: 
				self.head = curNode1

			curNode1.next, curNode2.next = curNode2.next, curNode1.next 

	def reverseLinkList( self): 
		if self.head is None: 
			return 
		else: 
			prevNode = None 
			curNode = self.head

			while curNode: 
				curNext = curNode.next
				curNode.next = prevNode
				prevNode = curNode
				curNode = curNext
			self.head = prevNode


			
sll = SingleLinkList()
sll.prepend( "Marge" )
sll.prepend( "Homer" )
sll.insert_after( "Bart","Marge" )
sll.append( "Lisa" )
sll.append( "Maggie" )
sll.traverse()
print( " " )
#sll.reverseLinkList()
#sll.traverse()
#print( " " )
print( sll.lenght )
sll.swapNodes( "Maggie", "Lisa")
print( " " )
sll.traverse()
sll.remove( "Maggie" )
print( " " )
sll.traverse()
sll.remove( "Homer" )
print( " " )
sll.traverse()
sll.remove( "Bart" )
print( " " )
sll.traverse()
print( " " )
print( sll.lenght ) 
sll.swapNodes( "Marge", "Lisa")
print( " " )
sll.traverse()
