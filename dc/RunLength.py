from dc.Common import Common

class RunLength(Common):

    # set the variables used in the calss
    def __init__(self):
        self.source = None
        self.encoded_string = ''

    # The algorithm
    def _count_(self):
        self.encoded_string = ''
        i=0
        while(i < len(self.source)):
            setVariable = self.source[i]
            count = 0
            while(self.source[i] == setVariable):
                count+=1
                i+=1
                if i >= len(self.source):
                    break
            self.encoded_string = self.encoded_string + str(count) + self.source[i-1]
            
            

    #the main function
    def compress(self, source):
        
        # get the source as string
        self.source = Common._setSource_(self,source)
        if self.source is None:
            Common._printError_(self)
            return        
        #get the distinct elements and their respective counts
        self._count_()

        return self.encoded_string

    

             
            