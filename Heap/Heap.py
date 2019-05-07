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
            temp=self._arr[i]
            self._arr[i]=self._arr[i//2]
            self._arr[i//2]=temp
            i=i//2
    
    def print_all(self):
        print(self._arr)

def test_Heap():
    print('初始化')
    sort=Heap(100)
    sort.print_all()
    #print('排序')
    #sort.sort()
    #sort.print_ordered()

if __name__=="__main__":
    test_Heap()
