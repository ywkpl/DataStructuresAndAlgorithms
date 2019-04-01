from typing import Optional

class Node:
    def __init__(self, data:object, next=None):
        self.data=data
        self.next=next
    @property
    def Data(self)->object:
        return self.data

class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.__pri="test"
    def insert_value_to_head(self, value:object):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
    
    def __iter__(self):
        node=self.head
        while node:
            yield node.data
            node=node.next
    
    def print_all(self):
        for item in self:
            print(item)

    def find_by_value(self, value:object)->Optional[Node]:
        p=self.head
        while p and not p.data.__eq__(value):
            p=p.next
        return p

    def find_by_index(self, index:int)->Optional[Node]:
        p=self.head
        position=0
        while p and position!=index:
            position+=1
            p=p.next
        return p


    def len(self)->int:
        i=0
        for item in self:
            i+=1
        return i

def test_singleLinkedList():
    link=SingleLinkedList()
    link.insert_value_to_head(12)
    link.insert_value_to_head(34)
    link.insert_value_to_head(24)
    link.print_all()
    assert link.len()==3

    findNode=link.find_by_value(24)
    assert link.find_by_value(24).data==24
    assert link.__pri=="test"

if __name__=="__main__":
    test_singleLinkedList()
    
    