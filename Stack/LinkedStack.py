from typing import TypeVar, Generic
T=TypeVar('T')
class Node(Generic[T]):
    def __init__(self, data:T, next=None):
        self.data=data
        self._next=next


class LinkedStack(Generic[T]):
    def __init__(self, capacity:int):
        self._capacity=capacity
        self._head=None
        self._len=0

    def push(self, value:T):
        if not value:
            return

        node=Node[T](value)
        self.push_node(node)

    def push_node(self, node:Node[T]):
        #栈满
        if self.is_full():
            print('栈满了！')
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

    def pop(self)->T:
        if self.is_empty():
            return
        
        if not self._head._next:
            val= self._head.data
            self._head=None
            self._len-=1
            return val
        
        val= self._head.data
        self._head=self._head._next
        self._len-=1
        return val

    def len(self):
        return self._len

    def print_all(self):
        if not self._head:
            return
        cur=self._head
        while cur:
            print(cur.data)
            cur=cur._next

def test_LinkedStack():
    print('初始化长度5整型栈')
    stack=LinkedStack[int](5)
    assert stack.is_empty()
    stack.push(2)
    stack.push(3)
    stack.push(5)
    stack.push(88)
    stack.push(9)
    assert stack.is_full()

    stack.print_all()
    print('满栈测试')
    val=stack.pop()
    print('出栈:'+str(val))
    val=stack.pop()
    print('出栈:'+str(val))
    val=stack.pop()
    print('出栈:'+str(val))
    print('出栈三次后：')
    stack.print_all()
    val=stack.pop()
    print('出栈:'+str(val))
    val=stack.pop()
    print('出栈:'+str(val))
    print('空栈测试')
    stack.pop()
    stack.print_all()

if __name__=="__main__":
    test_LinkedStack()