#堆
import random,time,math,numpy
class Heap:
    def __init__(self, capacity:int):
        self._count=0
        self._capacity=capacity
        self._arr=[]
        self._arr.insert(0, None)
        self._insert_values(1000000)

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self.insert(random.randint(1,100))

    def insert(self, data:int):
        #堆满
        if self._count>=self._capacity:
            return

        self._arr.append(data)
        self._count+=1
        i=self._count
        while i//2>0 and self._arr[i]>self._arr[i//2]:
            self._swap(i, i//2)
            i=i//2
    
    def _swap(self, i, j):
        temp=self._arr[j]
        self._arr[j]=self._arr[i]
        self._arr[i]=temp

    def delete(self):
        if self._count==0:
            return
        
        self._arr[1]=self._arr[self._count]
        self._arr.pop(self._count)
        self._count-=1

        i=1
        while True:
            maxPos=i
            if i*2<=self._count and self._arr[i]<self._arr[i*2]:
                maxPos=i*2
            
            if i*2+1<=self._count and self._arr[i]<self._arr[i*2+1]:
                if self._arr[i*2+1]>self._arr[i*2]:
                    maxPos=i*2+1
                
            if i==maxPos:
                break
            
            self._swap(i, maxPos)

    def print_all(self):
        print(self._arr)

def test_Heap():
    print('初始化')
    sort=Heap(10)
    sort.print_all()
    i=0
    while i<5:
        sort.delete()
        sort.print_all()
        i+=1
    sort.print_all()
    #print('排序')
    #sort.sort()
    #sort.print_ordered()

if __name__=="__main__":
    test_Heap()
