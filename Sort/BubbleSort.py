#冒泡排序
import random,time

class BubbleSort:
    def __init__(self, capacity:int):
        self._arr=[]
        self._insert_values(capacity)

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self._arr.append(random.randrange(1,100000, 2))

    def print_all(self):
        print(self._arr)

    def sort(self):
        start=time.time()
        arrlen=len(self._arr)
        if arrlen<=1: return
        i=0
        while i<arrlen-1:
            j=i+1
            while j<arrlen:
                if(self._arr[i]>self._arr[j]):
                    temp=self._arr[i]
                    self._arr[i]=self._arr[j]
                    self._arr[j]=temp
                j+=1
            i+=1
        end=time.time()
        print(end-start)

    def sort1(self):
        start=time.time()
        arrlen=len(self._arr)
        if arrlen<=1: return
        i=0
        while i<arrlen:
            j=0
            while j<arrlen-1:
                if(self._arr[j+1]<self._arr[j]):
                    temp=self._arr[j+1]
                    self._arr[j+1]=self._arr[j]
                    self._arr[j]=temp
                j+=1
            i+=1
        end=time.time()
        print(end-start)

def test_BubbleSort():
    # print('初始化')
    # sort=BubbleSort(1000)
    # sort.print_all()
    # print('排序')
    # sort.sort()
    # sort.print_all()

    print('第二种冒泡')
    sort=BubbleSort(20000)
    #sort.print_all()
    print('排序')
    sort.sort1()
    #sort.print_all()

if __name__=="__main__":
    test_BubbleSort()

