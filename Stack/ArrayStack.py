from typing import TypeVar, Generic
T=TypeVar('T')
class ArrayStack(Generic[T]):
    def __init__(self, capacity:int):
        self._capacity=capacity
        self._top=-1
        self._arr=[]

    def is_full(self)->bool:
        return self._capacity==self._top+1

    def push(self, value:T):
        if self.is_full():
            print('栈满！')
            return
        
        self._arr.append(value)
        self._top+=1

    def is_empty(self)->bool:
        return self._top==-1

    def pop(self)->T:
        if self.is_empty():
            print('栈空！')
            return

        val=self._arr.pop(self._top)
        self._top-=1
        return val

    def print_all(self):
        print(self._arr)
    
def test_ArrayStack():
    print('初始化长度5整型栈')
    stack=ArrayStack[int](5)
    assert stack.is_empty()
    stack.push(2)
    stack.push(3)
    stack.push(5)
    stack.push(88)
    stack.push(9)
    print('满栈测试')
    stack.push(111)
    assert stack.is_full()

    stack.print_all()
    
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
    test_ArrayStack()
        