
class DoubleLinkListNode: 
	def __init__( self, item ): 
		self.item  = item 
		self.next = None
		self.prev = None


class DoubleLinkList: 
	def __init__( self):
		self.head = None 
		self.lenght = 0 

	def prepend( self, item ): 
		if self.head is None: 
			self.head = DoubleLinkListNode( item )
		else: 
			newNode = DoubleLinkListNode( item )
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
		self.lenght += 1 

	def append( self, item ): 
		if self.head is None: 
			self.head = DoubleLinkListNode( item )
		else: 
			newNode = DoubleLinkListNode( item )			
			curNode = self.head 
			while curNode.next:				
				curNode = curNode.next
			curNode.next = newNode
			newNode.prev = curNode
		self.lenght += 1 

	def insert_after( self, item, prevNode):
		if self.head is None: 
			self.head = DoubleLinkListNode( item )
		else:
			newNode = DoubleLinkListNode( item )			
			curNode = self.head
			while curNode and curNode.item != prevNode: 			
				curNode = curNode.next			
			if curNode: 				
				curNode.next.prev = newNode
				newNode.next = curNode.next				
				curNode.next = newNode		
				newNode.prev = curNode	
	#Sigo trabajando en remover el elemento en el print
		self.lenght += 1 
				
	def traverse( self): 
		if self.head is None: 
			return 
		else: 
			self._traverse( self.head ) 
	
	def _traverse( self, curNode): 
		DoubleLinkList_ = ""
		while curNode: 
			DoubleLinkList_ += curNode.item	+ "--> "		
			curNode = curNode.next 
		print( DoubleLinkList_ , end="")

	def remove( self, item ):
		if self.head.item == item: 			
			self.head = self.head.next
			self.head.prev = None
		else: 			
			curNode = self.head
			while curNode and curNode.item != item: 				
				curNode = curNode.next
			if curNode:
				curNode.next.prev = curNode.prev								
				curNode.prev = curNode.next
		self.lenght -= 1 
	
	def reverseLinkList( self):
		if self.head is None: 
			return 
		else: 			
			curNode = self.head
			while curNode: 
				tmp = curNode.prev
				curNode.prev = curNode.next
				curNode.next = tmp 
				curNode = curNode.prev
			if tmp: 
				self.head = tmp.prev

dll = DoubleLinkList()
dll.prepend("Marge")
dll.prepend("Homer")
dll.append("Lisa")
dll.append("Maggie")
dll.traverse()
print( " " )
dll.insert_after("Bart","Marge")
dll.traverse()
print( " " )
dll.remove( "Bart" )
dll.traverse()
print( " " )
dll.reverseLinkList()
dll.traverse()
print( " " )
