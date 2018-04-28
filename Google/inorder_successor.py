#inorder successor means the number closest to the current node   e.g  if current node is 3, successor is 4

class Node(object):
	"""docstring for 
"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getChildren(self):
		children = []
		if (self.left != None):
			children.append(self.left)
		if (self.right != None):
			children.append(self.right)
		return children
		


class mytree(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.root = None

	
	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self.__insertNode(self.root, val)

#this is a private function, which can't be called outside the function 
	def __insertNode(self, currentN, val):
	#	print('val is ' + str(val) + ' currentN is ' + str(currentN.value))
		if currentN.value > val:
		#	print("Left node: " + str(currentN.left))
			if currentN.left == None:
				currentN.left = Node(val)
			else:
				self.__insertNode(currentN.left, val) 
		else:
		#	print("Right node: " + str(currentN.right))
			if currentN.right == None:
				currentN.right = Node(val)
			else:
				self.__insertNode(currentN.right, val)


	def leftTraverse(self, node):
		curnode = Node(node)
		while curnode is not None:
			if curnode.left is not None:
				print(curnode.value)
				curnode = curnode.left




	def inorderSuccessor(self,  node):
		l = []
		while self.root is not None:
			if self.root.left.value > node:
			#	nextL = self.root.left.value
				print('left node is ' + str(self.root.left.value))
				self.root = self.root.left
				
				# if nextL > node:
				# 	l.append(nextL)
				

			# if self.root.value <= node:
			# 	nextR = self.root.right.value
			# 	print("right node is " + str(nextR))
			# 	if nextR > node:
			# 		l.append(nextR)				

					
		if len(l) == 0 and self.root.value > node:
			l.append(self.root.value)

			return l


t = mytree()

t.insert(7)
t.insert(6)
t.insert(4)
t.insert(5)
t.insert(9)
t.insert(10)

t.inorderSuccessor(5)
#t.leftTraverse(6)



			#go to the left node and find the next left

def inOrder(t):
	# print(t)
	if t == None:
		return None
	else:
		#print('left node is' + str(t.left))	
		inOrder(t.left)
		print(t.value)
		inOrder(t.right)
		#print('right node is' + str(t.right))



t = mytree()

t.insert(7)
t.insert(4)
t.insert(5)
t.insert(9)
t.insert(10)

t.inorderSuccessor(3)

inOrder(t.root)


####example 
class foo:
	def __init__(self, bar, bar2):
		self.bar = bar
		self.bar2 = bar2

a = foo(foo(23,24),foo(25,26))

a.bar.bar


#recursion example, the key of recursion is to define the scope very well
def total(x):
	if x < 10 :
	#	print (n)
		return total(x+1)+total(x+2)
	else:
		return 0
	

def total(x):
	if x < 10 :
	#	print (n)
		return total(x+1)+2
	else:
		return 0
		

def total(x):
	if x < 10 & x >0:
		print (x)
		return total(x-1)*2
	else:
		return 0

###more on private function
class Foo(object):
	__bar = 99
	def __privatePrint(self):
		print(self.__bar)
	def PrintBar(self):
		self.__privatePrint()

a = Foo()
a.PrintBar()
a.__bar






