#跳表
import random,time

class Node:
    def __init__(self, data:int):
        self._data=data
        self._level=0
        self._nexts=[]
        

class SkipList:
    def __init__(self):
        self._MaxLevel=10
        self._head=initHead()

    def initHead(self):
        self._head=Node(-1)
        i=0
        while i<self._MaxLevel:
            self._head._nexts[i]=None
            i+=1
        
    def print_all(self):
        print(self._nodes)

    def insert(self, value:int):
        return

    def randomLevel(self)->int:
        return random.randint(1, self._MaxLevel-1)

def test_SkipList():
    # print('初始化')
    # sort=SkipList(1000)
    # sort.print_all()
    # print('排序')
    # sort.sort()
    # sort.print_all()

    print('第二种冒泡')
    sort=SkipList(20000)
    #sort.print_all()
    print('排序')
    sort.sort1()
    #sort.print_all()

if __name__=="__main__":
    test_SkipList()

