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
        newNode=Node(value)
        cur, prev=self._head, None
        while cur and cur.data!=searchValue:
            prev=cur
            cur=cur._next
        
        if not prev and cur:
            newNode._next=cur
            self._head=newNode
            self.__len+=1
            return

        if cur:
            newNode._next=cur
            prev._next=newNode
            self.__len+=1

    def delete_by_value_1(self, value:int):
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

    def delete_by_value(self, value:int):
        if not self._head or not value:
            return
        fake_head = Node(-1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        
        #解法比较巧妙，当current当前值等于删除值时，prev指针不移动，也就是会停在当前指针的前一个节点
        #然后current指针下移，这时候prev指针和current指针中间刚好是需要删除的节点，当进入下一个循环时
        #current值不等于删除值，这时将prev的next指针指向current指针节点，也就是跳过了删除节点，这段
        #因为如果删除的刚好是头节点，所以需要将头节点再次移至fake_head的next节点，也就是重置头指针，
        #有一个疑问，虽然链表已经删除了节点，但是删除节点的next还在，也就是单向断开链接，这样会不会造成无法垃圾回收呢？
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = fake_head._next  # in case head.data == value


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
    link.print_all()

if __name__=="__main__":
    test_singleLinkedList()
    
    