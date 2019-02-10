class Common:

    
    # returns a string if the source can be converted into a string
    def _setSource_(self,source):
        try:
            return str(source)
        except:
            print("Cannot be processed to String")
            return None
    
   

    # default error messsage
    def _printError_(self):
        print("Data Compression Not Successful")