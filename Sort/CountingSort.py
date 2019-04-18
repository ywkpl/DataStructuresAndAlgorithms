#計數排序，桶排序特殊情況,正整數
import random,time

class CountingSort:
    def __init__(self, capacity:int):
        self._arr=[]
        self._buckets=[]
        self._insert_values(capacity)
        
    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self._arr.append(random.randint(1,1000))

    def print_all(self):
        print(self._arr)

    #初始化计数桶数组
    def _init_bucket(self):
        max=self._arr[0]
        i=1
        while i<len(self._arr):
            if self._arr[i]>max:
                max=self._arr[i]
            i+=1
        self._buckets=[0 for x in range(max+1)]
        
    #统计数组个数
    def count_num(self):
        i=0
        while i<len(self._arr):
            self._buckets[self._arr[i]]+=1
            i+=1

    def total_num(self):
        i=1
        while i<len(self._buckets):
            self._buckets[i]=self._buckets[i-1]+self._buckets[i]
            i+=1        

    def sorting(self):
        temp=[0 for x in range(len(self._arr))]
        i=len(self._arr)-1
        while i>=0:
            index=self._buckets[self._arr[i]]-1
            temp[index]=self._arr[i]
            self._buckets[self._arr[i]]-=1
            i-=1
        #复制
        i=0
        while i<len(temp):
            self._arr[i]=temp[i]
            i+=1

    def sort(self):
        start=time.time()
        
        self._init_bucket()
        self.count_num()
        self.total_num()
        self.sorting()

        end=time.time()
        print(end-start)

def test_CountingSort():
    print('初始化')
    sort=CountingSort(10000000)
    #sort.print_all()
    print('排序')
    sort.sort()
    #sort.print_all()

if __name__=="__main__":
    test_CountingSort()
