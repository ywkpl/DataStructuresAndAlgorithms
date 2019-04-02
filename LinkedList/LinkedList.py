from typing import Optional

class Node:
    def __init__(self, data:object, next=None):
        self.data=data
        self.__next=next

class SingleLinkedList:
    def __init__(self):
        self.__head=None

    def insert_node_to_head(self, node:Node):
        node.__next=self.__head
        self.__head=node

    def insert_value_to_head(self, value:object):
        newNode=Node(value)
        self.insert_node_to_head(newNode)
    
    def delete_by_value(self, value:object):
        if not self.__head or not value:
            return
        prevNode=Node(-1)
        prevNode.__next=self.__head

        p=self.__head
        while p:
            print(prevNode.data)
            print(p.data)
            print(self.__head.data)
            prevNode=prevNode.__next
            p=p.__next


    def __iter__(self):
        node=self.__head
        while node:
            yield node.data
            node=node.__next
    
    def print_all(self):
        for item in self:
            print(item)

    def find_by_value(self, value:object)->Optional[Node]:
        p=self.__head
        while p and not p.data.__eq__(value):
            p=p.__next
        return p

    def find_by_index(self, index:int)->Optional[Node]:
        p=self.__head
        position=0
        while p and position!=index:
            position+=1
            p=p.__next
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
    link.insert_node_to_head(Node(33))
    assert link.len()==4

    findNode=link.find_by_value(24)
    assert findNode.data==24

    findNode=link.find_by_index(2)
    assert findNode.data==34
   
    link.delete_by_value(12)

if __name__=="__main__":
    test_singleLinkedList()
    
    