class Node: 
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


listed_list=LinkedList(10)
print(listed_list.head.value) # 10
print(listed_list.tail.value) # 10





