from typing import Optional

class Node:
    def __init__(self, data:int, next=None):
        self.data=data
        self._next=next

class SingleLinkedList:
    def __init__(self):
        self._head=None
        self.__len=0

    def insert_node_to_head(self, node:Node):
        node._next=self._head
        self._head=node
        self.__len+=1

    def insert_value_to_head(self, value:int):
        newNode=Node(value)
        self.insert_node_to_head(newNode)

    def insert_value_before(self, value:int, searchValue:int):
        if self._head.data==searchValue:
            self.insert_value_to_head(value)
            return

        newNode=Node(value)
        cur, prev=self._head._next, self._head
        while cur and cur.data!=searchValue:
            prev=cur
            cur=cur._next
        
        if cur:
            newNode._next=cur
            prev._next=newNode
            self.__len+=1

    def insert_value_after(self, value:int, searchValue:int):
        cur=self._head
        while cur and cur.data!=searchValue:
            cur=cur._next

        if cur:
            newNode=Node(value)
            if cur._next:
                newNode._next=cur._next
            cur._next=newNode
            self.__len+=1

    def insert_node_after(self, value:int, node:Node):
        if not node or not node.data:
            return
        self.insert_value_after(value, node.data)

    def delete_by_value(self, value:int):
        if not self._head or not value:
            return
        cur, prev=self._head, None
        
        while cur and cur.data!=value:
            prev=cur
            cur=cur._next

        if prev and prev._next:
            prev._next=cur._next

        if not prev:
            self._head=self._head._next if self._head._next else None
        
        if cur:
            cur=None
            self.__len-=1
            
    def len(self)->int:
        return self.__len

    def __iter__(self):
        node=self._head
        while node:
            yield node.data
            node=node._next
    
    def print_all(self):
        for item in self:
            print(item)

    def find_by_value(self, value:int)->Optional[Node]:
        p=self._head
        while p and not p.data==value:
            p=p._next
        return p

    def find_by_index(self, index:int)->Optional[Node]:
        p=self._head
        position=0
        while p and position!=index:
            position+=1
            p=p._next
        return p

def test_singleLinkedList():
    link=SingleLinkedList()
    link.insert_value_to_head(24)
    link.insert_node_to_head(Node(33))
    link.insert_value_to_head(56)
    assert link.len()==3

    findNode=link.find_by_value(24)
    assert findNode is not None

    findNode=link.find_by_index(2)
    assert findNode.data==24

    link.delete_by_value_1(33)

    link.insert_value_before(88, 24)
    link.insert_value_before(77, 56)
    link.insert_value_before(1, 88)
    

    link.insert_value_after(45, 77)
    link.insert_value_after(40, 56)
    link.insert_value_after(100, 24)
    link.print_all()

if __name__=="__main__":
    test_singleLinkedList()
    
    