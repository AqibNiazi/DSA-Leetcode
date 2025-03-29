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

linked_list=LinkedList(4)

print('Head:', linked_list.head.value)
print('Tail:', linked_list.tail.value)
print('Length:', linked_list.length)
