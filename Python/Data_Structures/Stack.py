
class Stack():	
	def __init__( self ):
		self.items = [] 

	def is_empty(self):
		return self.items == []

	def push( self, item ):
		self.items.append( item )

	def pop( self ):
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]

	def print_stack(self):
		return self.items

s = Stack()
print( s.is_empty())
s.push("Homer")
s.push("Marge")
s.push("Bart")
s.push("Lisa")
s.push("Maggie")
print( s.print_stack() ) 
s.pop()
print( s.print_stack() ) 
print( s.peek() ) 
print( s.print_stack() ) 
print( s.is_empty())

		