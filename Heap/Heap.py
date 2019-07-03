#堆
import random,time,math
class Heap:
    def __init__(self, capacity:int):
        self._count=0
        self._capacity=capacity
        self._arr=[]
        self._arr.insert(0, None)
        self._insert_values(1000000)

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self.insert(random.randint(1,100000))

    def insert(self, data:int):
        #堆满
        if self._count>=self._capacity:
            return

        self._arr.append(data)
        self._count+=1
        #堆化
        self.__heapify(self._count)
        
    
    def __heapify(self, i:int):
        while i//2>0 and self._arr[i]>self._arr[i//2]:
            self._swap(i, i//2)
            i=i//2

    def _swap(self, i, j):
        temp=self._arr[j]
        self._arr[j]=self._arr[i]
        self._arr[i]=temp

    def heapify_down(self, i:int):
        maxPos,j=1,1
        while True:
            #拥有左子树
            if j*2<=i:
                if self._arr[j]<self._arr[j*2]:
                    maxPos=j*2
            #拥有右子树
            if j*2+1<=i:
                if self._arr[maxPos]<self._arr[j*2+1]:
                    maxPos=j*2+1

            if j!=maxPos:
                self._swap(j,maxPos)
                j=maxPos
            else:
                break

    def sort(self):
        i=self._count
        start=time.time()
        while i>1:
            self._swap(i,1)
            i=i-1
            self.heapify_down(i)
        end=time.time()
        print(end-start)

    def delete(self):
        if self._count==0:
            return
        
        self._arr[1]=self._arr[self._count]
        self._arr.pop(self._count)
        self._count=self._count-1

        i=1
        #拥有左子树
        while i*2<=self._count:
            maxPos=i*2
            #拥有右子树
            if i*2+1<=self._count:
                if self._arr[i*2]<self._arr[i*2+1]:
                    maxPos=i*2+1
            #子树最大节点值大于父节点值，交换
            if self._arr[maxPos]>self._arr[i]:
                self._swap(maxPos, i)
                i=maxPos
            else:
                break

    def print_all(self):
        print(self._arr)

def test_Heap():
    print('初始化')
    sort=Heap(1000000)
    #sort.print_all()
    sort.sort()
    # print('排序后')
    # sort.print_all()
    # i=0
    # while i<5:
    #     sort.delete()
    #     sort.print_all()
    #     i+=1

    #print('排序')
    #sort.sort()
    #sort.print_ordered()

if __name__=="__main__":
    test_Heap()
