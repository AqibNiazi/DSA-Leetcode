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
        
    def append(self,value):
            new_node=Node(value)
            if self.length==0:
               self.head=new_node
               self.tail=new_node
            else:
                self.tail.next=new_node
                self.tail=new_node
            self.length+=1
            
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
       

linked_list=Linked_List(10)
linked_list.append(20)
linked_list.append(30)

linked_list.print_list()   

print("Head :", linked_list.head.value)    
print("Tail :", linked_list.tail.value)    