class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, expression):
        self.root = None
        self.add(expression)

    def add(self, expression):
        nums = '0123456789'
        num = ''
        token_list = []
        for n in expression:
            if n in nums:
                num+=n
            elif num:
                token_list.append(int(num))
                num = ''
                token_list.append(n)
            else:
                token_list.append(n)

        self.root = self._addToTree(token_list)

    def _addToTree(self, token_list):
        if token_list:
            brackets = 0
            index_sym = 0
            for inx, sym in enumerate(token_list):
                if sym == '(':
                    brackets += 1
                    if brackets == 1:
                        for i in range(len(token_list)):
                            if token_list[i] == ',' and i>=inx:
                                index_sym = i
                                break
                if sym == ')':
                    brackets -= 1
                    if brackets == 1:
                        for i in range(len(token_list)):
                            if token_list[i] == ',' and i>=inx:
                                index_sym = i
                                break

            return Node(token_list[0], self._addToTree(token_list[2:index_sym]),
                        self._addToTree(token_list[index_sym+1:-1]))
    def InOrder(self):
        self._InOrder(self.root)

    def _InOrder(self, node):
        if (node != None):
            self._InOrder(node.left)
            print( str(node.data), end= ' ' )
            self._InOrder(node.right)

    def PreOrder(self):
        self._PreOrder(self.root)

    def _PreOrder(self, node):
        if (node != None):
            print( str(node.data), end= ' ' )
            self._PreOrder(node.left)
            self._PreOrder(node.right)

    def PostOrder(self):
        self._PostOrder(self.root)

    def _PostOrder(self, node):
        if (node != None):
            self._PostOrder(node.left)
            self._PostOrder(node.right)
            print( str(node.data), end= ' ' )
                print( str(newNode), end= ' ' )
                if (newNode.right): stack.append(newNode.right)
                if (newNode.left): stack.append(newNode.left)
    def IterativePreorder(self):
        self._IterativePreorder(self.root)

    def _IterativePreorder(self, node):
        if (node != None):
            stack = []
            stack.append(node)
            while(stack):
                newNode = stack.pop()
                print( str(newNode), end= ' ' )
                if (newNode.right): stack.append(newNode.right)
                if (newNode.left): stack.append(newNode.left)

#main

tree = Tree('8(3(1,6(4,7)),10(,14(13,)))')


print('Прямой обход')
tree.PreOrder()

print('\n')
print('Концевой обход')
tree.PostOrder()

print('\n')
print('Центральный обход')
tree.InOrder()

print('\n')
print('Нерекурсивный прямой обход')
tree.IterativePreorder()
