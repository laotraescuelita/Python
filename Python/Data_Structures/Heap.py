class Heap:
	def __init__(self, size):
		self.size = size
		self.heap = []
		self.idx = -1
		

	def insert(self, data):
		#Insertar el valor en la ultima posición.
		self.heap.append( data )
		self.idx += 1
			
		#Aquí se invoca una función que acomoda el "array" para respestar la estructura del heap
		self.heappop( self.idx )
			
	def heappop(self, idx):
		while idx // 2 > 0:
			# SI el elemento es mayor que su padre hay que cambiar la posición.
			if self.heap[idx] > self.heap[idx // 2]:
			    self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
			# Hay que mover el indice del padre para continuar con la busqueda
			idx = idx // 2
	
	def heapsort(self):
		n = len(self.heap) - 1
		for i in range(n):
			self.heapify(i, n)
		
	def heapify(self, i, j):
		largest = i # Iniciar el indice como el que contiene el valor mas grande
		l = 2 * i + 1	 # izquierda = 2*i + 1
		r = 2 * i + 2	 # derecha = 2*i + 2

		# Mirar si hay hijo izquierdo y además es mayor que la su pdre.
		if l < j and self.heap[i] < self.heap[l]:
			#En ese caso el indice mayor sera el lado izquierdo
			largest = l

		# Mirar si el hijo derecho existe y es mayor que la raiz
		if r < j and self.heap[largest] < self.heap[r]:
			#En ese caso el maor sera el hijo derecho
			largest = r

		# Intercambiar los nodos si es necesario
		if largest != i:
			self.heap[i], self.heap[largest] = self.heap[largest],self.heap[i] # swap
			self.heapify(largest, j)
			
hp = Heap(7)

import numpy as np 
A = np.random.randint(0,30,7)

for i in A:
	hp.insert( i )

print( A )
print( hp.heap )
hp.heapsort()
print( hp.heap )
