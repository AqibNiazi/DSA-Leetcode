from typing import Any


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
        
linked_list=LinkedList(5)

print(linked_list.head.value) # 5
print(linked_list.tail.value) # 5   


