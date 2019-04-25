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
        i=self._level-1
        while i>=0:
            print('第'+str(i+1)+'层:')
            p=self._head
            pstr=''
            while p._nexts[i]:
                pstr+=str(p._nexts[i]._data)+' '
                p=p._nexts[i]
            print('['+pstr+']')
            i-=1
        
    def _insert(self, value:int):
        level=self.random_level()
        #新建节点
        newNode=self.create_node(value, level)
        prevNodes=[None for x in range(0, level)]
        # i=level-1
        # while i>=0:
        #     prevNodes[i]=self._head
        #     i-=1

        p=self._head
        i=level-1
        #查找所有阶层插入位置
        while i>=0:
            while p._nexts[i] and p._nexts[i]._data<value:
                p=p._nexts[i]
            prevNodes[i]=p
            i-=1

        #插入
        i=0
        while i<level:
            newNode._nexts[i]=prevNodes[i]._nexts[i]
            prevNodes[i]._nexts[i]=newNode
            i+=1

        #更新最大层阶
        if level>self._level: self._level=level

    def delete(self, value:int)->bool:
        p=self._head
        prevNodes=[None for x in range(0, self._level)]
        i=self._level-1
        while i>=0:
            while p._nexts[i] and p._nexts[i]._data<value:
                p=p._nexts[i]
            prevNodes[i]=p
            i-=1

        if p._nexts[0] and p._nexts[0]._data==value:
            p=p._nexts[0]
            i=0
            while i<p._level:
                prevNodes[i]._nexts[i]=p._nexts[i]
                i+=1
            p=None
            return True
        return False

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
    i=0
    while i<=1000:
        skipList._insert(random.randint(0,200))
        i+=1
    skipList.print_all()

    print('查找')
    searchNode=skipList.search(102)
    if searchNode:
        print(searchNode._data, searchNode._level)
    else:
        print('未找到')

    print('刪除')
    isDeleted=skipList.delete(8)
    if isDeleted:
        print('删除成功！')
    else:
        print('删除失败！')
    skipList.print_all()

if __name__=="__main__":
    test_SkipList()

