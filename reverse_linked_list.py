#Reverse a linked list

from typing import Optional

class Node:
    def __init__(self, val:int=0, next=None):
        self.val=val
        self.next=next

def traverse_ll(head:Optional[Node])->list[int]:
    current:Optional[Node]=head
    temp_list:list=[]
    while current:
        temp_list.append(current.val)
        current=current.next
    return temp_list    

def reverse_ll(head)->Optional[Node]:
    prev: Optional[Node] = None
    current: Optional[Node] = head
    while current:
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    return prev    
    
if __name__=="__main__":
    N1=Node(1)
    N2=Node(2)
    N3=Node(3)
    N1.next=N2
    N2.next=N3
    head:Optional[Node]=N1
    prev:Optional[Node]=reverse_ll(head)
    final_list:list[int]=traverse_ll(prev)
    print(final_list)
    