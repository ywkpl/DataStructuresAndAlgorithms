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
        self.initHead()

    def initHead(self):
        self._head=self.create_node(-1, self._MaxLevel)
        
    def print_all(self):
        i=self._MaxLevel-1
        while i>=0:
            print('第'+str(i+1)+'层:')
            p=self._head
            while p:
                print(p._data)
                p=p._nexts[i]
            i-=1

    def insert(self, value:int):
        level=self.random_level()
        #新建节点
        newNode=self.create_node(value, level)
        #查找插入节点
        prevNode=self.find_node(newNode)
        #插入节点
        self.insert_node(prevNode, newNode)

    def insert_node(self, prevNode:Node, insertNode:Node):
        i=insertNode._level-1
        #以插入节点高度链接，超出部分暂时未处理
        while i>=0:
            insertNode._nexts[i]=prevNode._nexts[i]
            prevNode._nexts[i]=insertNode
            i-=1

    def find_node(self, insertNode:Node)->Node:
        p=self._head
        i=p._level-1
        while i>0:
            #无后绪节点：下沉
            if not p._nexts[i]:
                i-=1
                continue
            
            #后绪节点值小于插入节点值，前进
            if p._nexts[i].data<insertNode._data:
                p=p._nexts[i]
                continue

            #后绪节点值大于插入节点值，节点找到
            if p._nexts[i].data>insertNode._data:
                break

        return p

    def create_node(self, value:int, level:int)->Node:
        node=Node(value)
        node._level=level
        node._nexts=[None for x in range(0, level)]
        return node

    def random_level(self)->int:
        level=1
        i=1
        while i<self._MaxLevel:
            randomNum=random.randint(0, self._MaxLevel)
            if randomNum % 2==0:
                i+=1
        return level

def test_SkipList():
    skipList=SkipList()
    skipList.insert(10)
    skipList.insert(5)
    skipList.insert(15)
    skipList.insert(12)
    skipList.insert(9)
    skipList.print_all()

if __name__=="__main__":
    test_SkipList()

