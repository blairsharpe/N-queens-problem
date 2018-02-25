class Stack(object):
    
    def __init__(self):
        
        self.__stack_List = []
    
    def push(self,coordinate):
        
        self.__stack_List.append(coordinate)
        return(True)       
    
    def pop(self):
        
        if(self.isEmpty() == False):
            
            coordinate = self.__stack_List.pop()
            return(coordinate)
        else:
            return(False)
    def isEmpty(self):
        
        if(self.__stack_List == None):
            return(True)
        else:
            return(False)
        
    def printStack(self):
        
        for i in self.__stack_List:
            print(i, end=' ')
