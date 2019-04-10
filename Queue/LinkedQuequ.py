from typing import TypeVar, Generic
T=TypeVar('T')
class Node(Generic[T]):
    def __init__(self, data:T, next=None):
        self.data=data
        self._next=next


class LinkedQueue(Generic[T]):
    def __init__(self, capacity:int):
        self._capacity=capacity
        self._head=None
        self._len=0

    def enqueue(self, value:T):
        if not value:
            return

        node=Node[T](value)
        self.enqueue_node(node)

    def enqueue_node(self, node:Node[T]):
        #队列满
        if self.is_full():
            print('队列满了！')
            return

        if not self._head:
            self._head=node
            self._len+=1
            return

        node._next=self._head
        self._head=node
        self._len+=1

    def is_empty(self)->bool:
        return self._len==0

    def is_full(self)->bool:
        return self._len==self._capacity

    def dequeue(self):
        if self.is_empty():
            return
        
        if not self._head._next:
            self._head=None
            self._len-=1
            return
        
        prev=self._head
        while prev._next._next:
            prev=prev._next

        prev._next=None
        self._len-=1

    def len(self):
        return self._len

    def print_all(self):
        if not self._head:
            return
        cur=self._head
        while cur:
            print(cur.data)
            cur=cur._next

def test_LinkedQueue():
    print('初始化长度5整型队列')
    queue=LinkedQueue[int](5)
    assert queue.is_empty()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(88)
    queue.enqueue(9)
    assert queue.is_full()

    queue.print_all()
    print('满队列测试')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print('出队列三次后：')
    queue.print_all()
    print('再进一次队：')
    queue.enqueue(456)
    queue.print_all()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print('空队列测试')
    queue.dequeue()
    queue.print_all()

if __name__=="__main__":
    test_LinkedQueue()