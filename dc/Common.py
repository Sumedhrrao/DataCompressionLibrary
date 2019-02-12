class Common:

    
    # returns a string if the source can be converted into a string
    def _setSource_(self,source):
        try:
            return str(source)
        except:
            print("Cannot be processed to String")
            return None
    
   # get probability of a cahracter in the string
    def _getProbability_(self,char,source):
        count = 0
        for i in source:
            if i == char:
               count+=1
            else:
               pass
        try:
            probability = (count/len(source)) * 100
        except:
            print("unable to get probabilty of element")
            return None
        return probability

    # get all the distinct elements in the string as list
    def _getDistinctSymbols_(self,source):
        try:
            set(source)
        except:
            print("unable to get distinct")
            return None
        return set(source)
    # default error messsage
    def _printError_(self):
        print("Data Compression Not Successful")

    