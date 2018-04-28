
# class equation():
#     def __init__(self, a, b, operand, num):
#         self.a = a
#         self.b = b
#         self.operand = operand
#         self.num = num


#     def getA(self):


class equation(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
   
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def addRightLink(self, newright):
        self.right = newright

    def addLeftLink(self, newleft):
        self.right = newleft
   
    def setVal(self, num):
        self.data = num

    # def find_Node(self,val):
    #     if val == root.data

    # def find(self,val):
    #     return self.find_Node(self.root, val)



####iterate branch

    def __iter__(self):
        if self.right != None:
            for i in self.right:
                yield i

        yield self

        if self.left != None:
            for i in self.left:
                yield i

        yield self

    # def traverse(self):
    #     if self.right != None:
    #         traverse(self.right)

    #     print(self)


       
root = equation()
root.data = "root"
root.left = equation()
root.left.data = "left"
root.right = equation()
root.right.data = "right1"
root.right.data = "right2"
root.right.data = "2"
#root.right.left = "c"

    

for node in root:
    print(node.data)

#################################################

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


left = Tree(2)
right = Tree(3)
tree = Tree(2, left,right)



def total(tree):
    if tree == None: 
        return 0
    else: 
        return total(tree.left) + total(tree.right) + tree.cargo


## 1+2*3
tree = Tree("+", Tree(1),Tree("*", Tree(2),Tree(3)))


#preorder traverse
def print_tree(tree):
    if tree == None:
        return None
    else:
        print (tree.cargo)
        print_tree(tree.left)
        print_tree(tree.right)



def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print tree.cargo


def isOperator(val):
    if val == '*' or val == "+" or val == "-" or val == "/":
        print ("True")
    else:
        print("False")

#A*B-C    AB*C-

def constructTree(postfix):
    l = []
    for char in postfix:
        if isOperator(char) == "False":
            l.append(char)
            #AB
            print(l)
        else:
            t1 = postfix[len(postfix)-1]
            t2 = postfix[len(postfix)-2]
        #make them as nodes
            Etree = Tree(1,t1,t2)


Etree = constructTree("A*B-C")
print_tree(Etree)








