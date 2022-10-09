class Queue():
    #初始化
    def __init__(self): 
        self.__items = []
    #队内元素数量    
    def size(self): 
        return len(self.__items)
    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    #入队    
    def push(self,element): 
        self.__items.append(element)
    #出队    
    def pop(self):  
        try:
            return self.__items.pop(0)
        except:
            print('ERROR:Stack is empty now!')
    #取队首        
    def head(self): 
        try:
            return self.__items[0]
        except:
            print('ERROR:Stack is empty now!')
    #取队尾        
    def tail(self): 
        try:
            return self.__items[-1]
        except:
            print("ERROR:Stack is empty now!")

q = Queue()
q.push(1)
print(q.pop())
print(q.pop())
print('************')
q.push(3.5)
q.push(2.7)
print(q.head())
print(q.size())
print(q.isEmpty())
