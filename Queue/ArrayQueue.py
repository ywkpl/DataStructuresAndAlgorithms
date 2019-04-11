from typing import TypeVar, Generic
T=TypeVar('T')
class ArrayQueue(Generic[T]):
    def __init__(self, capacity:int):
        self._capacity=capacity
        self._top=-1
        self._arr=[]

    def is_full(self)->bool:
        return self._capacity==self._top+1

    def enqueue(self, value:T):
        if self.is_full():
            print('队列满！')
            return
        
        self._arr.insert(0, value)
        self._top+=1

    def is_empty(self)->bool:
        return self._top==-1

    def dequeue(self)->T:
        if self.is_empty():
            print('队列空！')
            return
        val=self._arr.pop(self._top)
        self._top-=1
        return val

    def print_all(self):
        print(self._arr)

def test_ArrayQueue():
    print('初始化长度5整型队列')
    queue=ArrayQueue[int](5)
    assert queue.is_empty()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(88)
    queue.enqueue(9)
    assert queue.is_full()

    queue.enqueue(100)
    queue.print_all()
    print('满队列测试')
    queue.dequeue()
    queue.print_all()
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
    test_ArrayQueue()