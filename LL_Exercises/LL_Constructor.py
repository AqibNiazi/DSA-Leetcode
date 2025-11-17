class Node:
    def __init__(self, value):
      self.value=value
      self.next=None
      

class Linked_List:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
my_linked_list = Linked_List(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)