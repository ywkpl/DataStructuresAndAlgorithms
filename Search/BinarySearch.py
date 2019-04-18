#二分查找法
import random, os, sys
sys.path.insert(0, os.path.abspath(".."))
from Sort.QuickSort import QuickSort

class BinarySearch:
    def __init__(self, capacity:int):
        sorted=QuickSort(capacity)
        sorted.sort()

        self._arr=sorted._arr
        self._value=0
    
    def _search(self, value:int)->int:
        self._value=value
        return self._search_recursion(0, len(self._arr)-1)

    def print_all(self):
        print(self._arr)

    def _search_recursion(self, start:int, end:int)->int:

        if start>end: return -1
        
        mid=start+(end-start)//2
        if self._arr[mid]==self._value: 
            return mid
        elif self._arr[mid]<self._value:
            return self._search_recursion(mid+1, end)
        else:
            return self._search_recursion(start, mid-1)
    
def test_BinarySearch():
    print('初始化')
    search=BinarySearch(100000)
    #search.print_all()
    index=search._search(200)
    if index==-1:
        print('未找到')
    else:
        print('找到，索引在'+str(index))
        print(search._arr[index])
    
if __name__=="__main__":
    test_BinarySearch()
