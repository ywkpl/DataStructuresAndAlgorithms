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
        self._level=1

    def initHead(self):
        self._head=self.create_node(-1, self._MaxLevel)
        
    def print_all(self):
        i=0
        while i<self._level:
            print('第'+str(i+1)+'层:')
            p=self._head
            while p:
                print(p._data)
                p=p._nexts[i]
            i+=1
        
    def _insert(self, value:int):
        level=self.random_level()
        #新建节点
        newNode=self.create_node(value, level)
        
        p=self._head
        i=self._MaxLevel-1
        #查找所有阶层插入位置
        prevNodes=[None for x in range(0, self._MaxLevel)]
        while i>=0:
            while p._nexts[i] and p._nexts[i]._data<value:
                p=p._nexts[i]
            i-=1
            prevNodes[i]=p
        
        #插入
        i=0
        while i<level:
            newNode._nexts[i]=prevNodes[i]._nexts[i]
            prevNodes[i]._nexts[i]=newNode
            i+=1

        #更新最大层阶
        if level>self._level: self._level=level

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

    def search(self, value:int)->Node:
        p=self._head
        i=self._level-1
        while i>=0:
            #节点不为空且节点值小于当前值，前进
            while p._nexts[i] and p._nexts[i]._data<value:
                p=p._nexts[i]
            #下沉
            i-=1

        if p._nexts[0] and p._nexts[0]._data==value:
            return p._nexts[0]
        else:
            return None

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
                level+=1
            i+=1
        return level

def test_SkipList():
    skipList=SkipList()
    skipList._insert(10)
    skipList._insert(5)
    skipList._insert(15)
    skipList._insert(12)
    skipList._insert(9)
    skipList.print_all()

    print('查找')
    searchNode=skipList.search(102)
    if searchNode:
        print(searchNode._data, searchNode._level)
    else:
        print('未找到')

if __name__=="__main__":
    test_SkipList()

