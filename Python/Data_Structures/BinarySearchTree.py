class BSTNode: 
	def __init__(self, item ): 
		self.item = item 
		self.left = None 
		self.right = None 


class BinarySearchTree:
	def __init__(self): 
		self.root = None 

	def insert(self, item): 
		if self.root is None: 
			self.root = BSTNode( item )
		else: 
			self._insert( item , self.root)

	def _insert( self, item, curNode): 
		
		if item < curNode.item: 
			if curNode.left: 
				self._insert( item, curNode.left)
			else: 
				curNode.left = BSTNode( item )
		
		elif item > curNode.item: 
			if curNode.right: 
				self._insert(item, curNode.right)
			else: 
				curNode.right = BSTNode( item )

	def remove(self, item): 
		if self.root is None: 
			return
		else: 
			self._remove(item, self.root)

	def _remove(self, item, curNode): 
	
		#if not curNode:
		#	return curNode

		if item < curNode.item: 
			if curNode.left:
				curNode.left = self._remove( item, curNode.left )
		
		elif item > curNode.item: 
			if curNode.right:
				curNode.right = self._remove( item, curNode.right )
		
		else: 
			if curNode.left is None and  curNode.right is None: 
				print( "Removing a leaf")
				del curNode
				return None 
			
			elif curNode.left is None: 
				print( "Removing a node with right child")
				tmpNode = curNode.right
				del curNode
				return tmpNode

			elif curNode.right is None: 
				print( "Removing a node with left child")
				tmpNode = curNode.left
				del curNode
				return tmpNode

			else:
				print( "Removing a node with both children ")
				tmpNode = self.getPredecesor( curNode.right )
				curNode.item = tmpNode.item
				curNode.right = self._remove( tmpNode.item, curNode.right )

		return curNode

	def getPredecesor( self, curNode): 
		if curNode.left: 
			return self.getPredecesor(curNode.left)
		return curNode


	def getMinValue(self): 
		if self.root is None: 
			return 
		else: 
			self._getMinValue(self.root)

	def _getMinValue( self, curNode ):
		if curNode.left: 
			return self._getMinValue(curNode.left)
		print( curNode.item )

	def getMaxValue(self): 
		if self.root is None: 
			return 
		else: 
			self._getMaxValue(self.root)

	def _getMaxValue( self,curNode ):
		if curNode.right: 
			return self._getMaxValue(curNode.right)
		print( curNode.item )

	def inOrderTraverse( self ):
		if self.root is None: 
			return 
		else:
			self._inOrderTraverse( self.root)

	def _inOrderTraverse( self, curNode): 
		if curNode: 
			print( curNode.item )
			self._inOrderTraverse( curNode.left )
			self._inOrderTraverse( curNode.right )

	def preOrderTraverse( self ):
		if self.root is None: 
			return 
		else:
			self._preOrderTraverse( self.root )

	def _preOrderTraverse( self, curNode): 
		if curNode: 			
			self._inOrderTraverse( curNode.left )
			print( curNode.item )
			self._inOrderTraverse( curNode.right )

	def postOrderTraverse( self ):
		if self.root is None: 
			return 
		else:
			self._postOrderTraverse( self.root )

	def _postOrderTraverse( self, curNode): 
		if curNode: 			
			self._postOrderTraverse( curNode.left )			
			self._postOrderTraverse( curNode.right )
			print( curNode.item )

bst = BinarySearchTree() 
bst.insert(8)
bst.insert(6)
bst.insert(9)
bst.insert(5)
bst.insert(10)
bst.inOrderTraverse()
print( " " )
bst.preOrderTraverse()
print( " " )
bst.postOrderTraverse()
print( " " )
bst.getMaxValue()
bst.getMinValue()
print( " " )
bst.remove(8)
bst.inOrderTraverse()
print( " " )
