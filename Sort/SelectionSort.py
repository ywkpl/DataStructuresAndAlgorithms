#选择排序
import random,time

class SelectionSort:
    def __init__(self, capacity:int):
        self._arr=[]
        self._insert_values(capacity)

    def _insert_values(self, capacity:int):
        for x in range(capacity):
            self._arr.append(random.randint(1,100000))

    def print_all(self):
        print(self._arr)

    def sort(self):
        start=time.time()
        arrlen=len(self._arr)
        if arrlen<=1: return
        i=0
        while i<arrlen-1:
            min,index=self._arr[i+1],i+1
            j=i+2
            while j<arrlen:
                if min>self._arr[j]:
                    min=self._arr[j]
                    index=j
                j+=1
            self._arr[index]=self._arr[i]
            self._arr[i]=min
            i+=1
                
        end=time.time()
        print(end-start)

def test_SelectionSort():
    print('初始化')
    sort=SelectionSort(20000)
    sort.print_all()
    print('排序')
    sort.sort()
    sort.print_all()

if __name__=="__main__":
    test_SelectionSort()

