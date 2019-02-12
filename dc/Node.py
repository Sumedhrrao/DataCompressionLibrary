class Node:
    
    def __init__(self,symbol,value):
        self.prev = None
        self.nextleft = None
        self.nextright = None
        self.value = value
        self.symbol = symbol
        self.code = ''
    
    def _setPrevNode_(self, node):
        prev = Node(self.symbol+node.symbol,self.value+node.value)
        prev.nextleft = self
        prev.nextright = node
        return prev

    def _printBinaryTree_(self):
        if(self.nextright == None):
            return
        self.nextright._printBinaryTree_()
        self.nextleft._printBinaryTree_()   
    
def _findSymbol_(self,symbol,code):
    code = code + ''
    if self.symbol == symbol:
        return code
    else:
        if symbol in self.nextleft.symbol:
            code = code + '0'
            return _findSymbol_(self.nextleft,symbol,code)
        else:
            code = code + '1'
            return _findSymbol_(self.nextright,symbol,code)



