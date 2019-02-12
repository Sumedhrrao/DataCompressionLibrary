from dc.Common import Common
from dc.Node import Node
from dc.Node import _findSymbol_
class Huffman(Common):

    def getProbability(self):
        self.dict_of_probabilities = {}
        set_of_uniques = Common._getDistinctSymbols_(self,self.source)
        for i in set_of_uniques:
            probability = Common._getProbability_(self,i,self.source)
            self.dict_of_probabilities[i] = probability
  
    
    def _setLeafNodes_(self):
        self.list_of_nodes = []
        for key,value in self.dict_of_probabilities.items():
            temp = Node(key,value)
            self.list_of_nodes.append(temp)
        self.list_of_nodes=sorted(self.list_of_nodes,key=lambda x:x.value)
        
    def _getLowestNodes_(self):
        self.list_of_nodes.reverse()
        while(len(self.list_of_nodes)!=1):
            
            if len(self.list_of_nodes) == 2:
                prev = self.list_of_nodes[2-1]._setPrevNode_(self.list_of_nodes[2-2])
                self.list_of_nodes.pop()
                self.list_of_nodes.pop()
                self.list_of_nodes.append(prev)
                break
            length = len(self.list_of_nodes)-1



            if((self.list_of_nodes[length - 0].value+self.list_of_nodes[length - 1].value)>(self.list_of_nodes[length - 1].value+self.list_of_nodes[length - 2].value)):
                prev = self.list_of_nodes[length - 1]._setPrevNode_(self.list_of_nodes[length - 2])
                temp = self.list_of_nodes[length]
                self.list_of_nodes.pop()
                self.list_of_nodes.pop()
                self.list_of_nodes.pop()
                self.list_of_nodes.append(prev)
                self.list_of_nodes.append(temp)
            
            else:
                prev = self.list_of_nodes[length - 0]._setPrevNode_(self.list_of_nodes[length - 1])
                self.list_of_nodes.pop()
                self.list_of_nodes.pop()
                self.list_of_nodes.append(prev)
    
    def getCodes(self):
            self.dict_of_codes = {}
            for key in self.dict_of_probabilities.keys():
                a = _findSymbol_(self.list_of_nodes[0],key,'')
                self.dict_of_codes[key] = a
    
    def encode(self):
        self.encoded = ''
        for i in self.source:
            self.encoded = self.encoded+self.dict_of_codes[i]


    def compress(self,source):
        self.source = Common._setSource_(self,source)
        self.getProbability()
        self._setLeafNodes_()
        self._getLowestNodes_()
        self.getCodes()
        self.encode()
        return self.encoded