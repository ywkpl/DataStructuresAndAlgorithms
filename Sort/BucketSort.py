#桶排序,线性排序
import random,time,math,numpy

class BucketSort:
    def __init__(self, capacity:int):
        self._arr=[]
        self._min=0
        self._max=0
        self._buckets=100
        self._step=0
        self._insert_values(capacity)
        self.set_values()
        self._bucket=[]
        self._ordered=[]

    def set_values(self):
        self._min, self._max=self._arr[0], self._arr[0]
        i=1
        while i<len(self._arr):
            if self._arr[i]<self._min:
                self._min=self._arr[i]
            if self._arr[i]>self._max:
                self._max=self._arr[i]
            i+=1
        self._step=math.ceil((self._max-self._min+1)/self._buckets) 
        
    def split_bucket(self, bucketIndex:int):
        if bucketIndex<1: return
        self.split_bucket(bucketIndex-1)
        minval=self._min+(bucketIndex-1)*self._step
        maxval=self._min+bucketIndex*self._step
        self._bucket=[]
        i=0
        while i<len(self._arr):
            if self._arr[i]>=minval and self._arr[i]<maxval:
                self._bucket.append(self._arr[i])
                #移除已加入桶數量，因為python二維數組未掌握而加入的效率方式
                self._arr.pop(i)
                continue
            i+=1
        
        #對桶進行快排
        self.quick_sort_bucket()
        
        #加入最終數組
        self._ordered=numpy.append(self._ordered, self._bucket)

    def quick_sort_bucket(self):
        self.sort_split(0, len(self._bucket)-1)

    def sort_split(self, start:int, end:int):
        if start>=end: return

        splitIndex=self.partition(start, end)
        self.sort_split(start, splitIndex-1)
        self.sort_split(splitIndex+1, end)

    def switch(self, i, j):
        temp=self._bucket[i]
        self._bucket[i]=self._bucket[j]
        self._bucket[j]=temp

    def partition(self, start:int, end:int)->int:
        pivot=self._bucket[end]
        i, j=start,start
        while j<end:
            if self._bucket[j]<pivot:
                self.switch(i, j)
                i+=1
            j+=1
        self.switch(i, j)
        return i

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self._arr.append(random.randint(1,500))

    def print_all(self):
        print(self._arr)

    def print_ordered(self):
        print(self._ordered)

    def sort(self):
        start=time.time()
        # i=1
        # while i<=self._buckets:
        #     self.split_bucket(i)
        #     i+=1
        self.split_bucket(self._buckets)
        end=time.time()
        print(end-start)

def test_BucketSort():
    print('初始化')
    sort=BucketSort(100000)
    #sort.print_all()
    print('排序')
    sort.sort()
    #sort.print_ordered()

if __name__=="__main__":
    test_BucketSort()


