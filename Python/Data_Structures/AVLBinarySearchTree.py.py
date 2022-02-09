class Node:
    def __init__( self, data):
        self.data = data 
        self.height = 1
        self.left = None
        self.right = None 
        

class AVL_Tree:
    def __init__(self):
        self.root = None 
    
    #Es necesario calcular la nueva altura de cada nodo ya que comienza como cero pero va cambiando conformo mas nodos se agregan
    def height(self, node):
        if node is None:
            return 0 
        return node.height
    
    #Si el valor devuelto es mayor que 1 significa que es una situacion cargada a la izquierda.
    #Si el valor devuelto es menor que 1 significa que es una situacion cargada a la derecha.
    def isbalanced(self, node):
        if node is None:
            return 0 
        return self.height(node.left) - self.height(node.right)

    #Rotar los nodos
    def rightrotation(self, node):
        print( "Right rotation ")
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        
        #Aquí se calcula la nueva altura del nodo
        node.height = max ( self.height(node.left), self.height(node.right)) + 1
        a.height = max( self.height(a.left), self.height(a.right)) + 1
        
        return a
    
    def leftrotation(self, node):
        print( "Left rotation ")
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        
        node.height = max ( self.height(node.left), self.height(node.right)) + 1
        a.height = max( self.height(a.left), self.height(a.right)) + 1
                
        return a
    
    #insertar un nuevo valor en el arbol
    def insert(self, data):
        self.root = self._insert( data, self.root)
    
    def _insert(self, data, curnode):

        if curnode is None:
            return Node( data )

        if data < curnode.data:            
            curnode.left = self._insert( data, curnode.left)
        else: 
            curnode.right = self._insert( data, curnode.right)

        curnode.height = max( self.height(curnode.left), self.height(curnode.right) ) + 1 
        return self.validateAVL( data, curnode )
     

    def validateAVL( self, data, curnode):
        
        balance = self.isbalanced( curnode )
                
        if balance > 1 and  data < curnode.left.data:
            return self.rightrotation( curnode )
        
        if balance > 1 and data > curnode.left.data:
            curnode.left = self.leftrotation( curnode.left )
            return self.rightrotation( curnode )
        
        if balance < -1 and data > curnode.right.data:
            return self.leftrotation( curnode )
    
        if balance < -1 and data < curnode.right.data:
            curnode.right = self.rightrotation( curnode.right )
            return self.leftrotation( curnode )

        return curnode

    def inOrderTraverse( self ):
        if self.root is None: 
            return 
        else:
            self._inOrderTraverse( self.root)

    def _inOrderTraverse( self, curnode): 
        if curnode: 
            print( curnode.data, curnode.height )
            self._inOrderTraverse( curnode.left )
            self._inOrderTraverse( curnode.right )

    def preOrderTraverse( self ):
        if self.root is None: 
            return 
        else:
            self._preOrderTraverse( self.root )

    def _preOrderTraverse( self, curnode): 
        if curnode:             
            self._inOrderTraverse( curnode.left )
            print( curnode.data, curnode.height )
            self._inOrderTraverse( curnode.right )

    def postOrderTraverse( self ):
        if self.root is None: 
            return 
        else:
            self._postOrderTraverse( self.root )

    def _postOrderTraverse( self, curnode): 
        if curnode:             
            self._postOrderTraverse( curnode.left )         
            self._postOrderTraverse( curnode.right )
            print( curnode.data, curnode.height )

    def remove(self, data): 
        if self.root is None:
            return
        else: 
            self._remove(data, self.root)

    def _remove(self, data, curnode): 

        if not curnode:
            return curnode

        if data < curnode.data:         
           curnode.left = self._remove( data, curnode.left )
        elif data > curnode.data:           
            curnode.right = self._remove( data, curnode.right )
        else: 
            
            if curnode.left is None and  curnode.right is None: 
                print( "Removing a leaf")
                del curnode
                return None 
            
            elif curnode.left is None: 
                print( "Removing a node with right child")
                tmpNode = curnode.right
                del curnode
                return tmpNode

            elif curnode.right is None: 
                print( "Removing a node with left child")
                tmpNode = curnode.left
                del curnode
                return tmpNode

            else:
                print( "Removing a node with both children ")
                tmpNode = self.getPredecesor( curnode.right )
                curnode.data = tmpNode.data
                curnode.right = self._remove( tmpNode.data, curnode.right )

        curnode.height = max( self.height(curnode.left), self.height(curnode.right) ) + 1
        return self.validateAVL(data, curnode)

    def getPredecesor( self, curnode): 
        if curnode.left: 
            return self.getPredecesor(curnode.left)
        return curnode

A = [10,20,30,40] #Left Rotation
#A = [30,20,10] #right Rotation
#A = [30,10,20] #rightLeft Rotation
#A = [10,30,20] #right Rotation

avl = AVL_Tree()
for i in A:
    avl.insert( i )

avl.inOrderTraverse()
avl.remove(20)
avl.inOrderTraverse()