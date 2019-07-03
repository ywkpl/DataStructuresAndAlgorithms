#快速排序,分而治之
import random,time,sys



class QuickSort:
    def __init__(self, capacity:int):
        self._arr=[]
        self._insert_values(capacity)

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self._arr.append(random.randint(1,100000))

    def print_all(self):
        print(self._arr)

    def sort_split(self, start:int, end:int):
        if start>=end: return

        splitIndex=self.partition(start, end)
        self.sort_split(start, splitIndex-1)
        self.sort_split(splitIndex+1, end)

    def switch(self, i, j):
        temp=self._arr[i]
        self._arr[i]=self._arr[j]
        self._arr[j]=temp

    def partition(self, start:int, end:int)->int:
        pivot=self._arr[end]
        i, j=start,start
        while j<end:
            if self._arr[j]<pivot:
                self.switch(i, j)
                i+=1
            j+=1
        self.switch(i, j)
        return i

    def sort(self):
        start=time.time()
        self.sort_split(0, len(self._arr)-1)
        end=time.time()
        print(end-start)

def test_QuickSort():
    print('初始化')
    sort=QuickSort(1000000)
    #sort.print_all()
    print('排序')
    sort.sort()
    #sort.print_all()

if __name__=="__main__":
    test_QuickSort()

