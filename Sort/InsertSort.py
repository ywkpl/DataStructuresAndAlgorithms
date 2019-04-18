#插入排序
import random,time

class InsertSort:
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
            value, j=self._arr[i+1], i
            while j>=0:
                if value<self._arr[j]:
                    self._arr[j+1]=self._arr[j]
                else:
                    break
                j-=1
            self._arr[j+1]=value
            i+=1
                
        end=time.time()
        print(end-start)

def test_InsertSort():
    print('初始化')
    sort=InsertSort(100000)
    #sort.print_all()
    print('排序')
    sort.sort()
    #sort.print_all()

if __name__=="__main__":
    test_InsertSort()

