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

    def search_last(self, value:int)->int:
        self._value=value
        return self.search_last_recursion(0, len(self._arr)-1)

    def search_last_recursion(self, start:int, end:int)->int:
        if start>end:return -1
        
        mid=start+(end-start)//2
        if self._arr[mid]==self._value:
            #如果是最后一个数或后面的数值不等于查找数，则证明当前数是最后一个数值,否则最后一个数值就在mid+1------start区间类
            if mid==len(self._arr)-1 or self._arr[mid+1]!=self._value:
                return mid
            return self.search_last_recursion(mid+1, end)    
        elif self._arr[mid]<self._value:
            return self.search_last_recursion(mid+1, end)
        else:
            return self.search_last_recursion(start, mid-1)

    def search_greaterthan(self, value:int)->int:
        self._value=value
        return self.search_greaterthan_recursion(0, len(self._arr)-1)

    def search_greaterthan_recursion(self, start:int, end:int)->int:
        if start>end:return -1
        
        mid=start+(end-start)//2
        if self._arr[mid]<self._value:
            return self.search_greaterthan_recursion(mid+1, end)
        else:
            #如果是第一个数或前面的数值小于查找数，则证明当前数是第一个大于等于数值,否则第一个大于等于数值就在start------mid-1区间类
            if mid==0 or self._arr[mid-1]<self._value:
                return mid
            return self.search_greaterthan_recursion(start, mid-1)

    def search_lessthan(self, value:int)->int:
        self._value=value
        return self.search_lessthan_recursion(0, len(self._arr)-1)

    def search_lessthan_recursion(self, start:int, end:int)->int:
        if start>end:return -1
        
        mid=start+(end-start)//2
        if self._arr[mid]>self._value:
            return self.search_lessthan_recursion(start, mid-1)
        else:
            #如果是最后一个数或后面的数值大于查找数，则证明当前数是最后一个小于等于数值,否则最后一个大于等于数值就在mid+1------start区间类
            if mid==len(self._arr)-1 or self._arr[mid+1]>self._value:
                return mid
            return self.search_lessthan_recursion(mid+1, end)

    def search_first(self, value:int)->int:
        self._value=value
        return self.search_first_recursion(0, len(self._arr)-1)

    def search_first_recursion(self, start:int, end:int)->int:
        if start>end:return -1
        
        mid=start+(end-start)//2
        if self._arr[mid]==self._value:
            #如果是第一个数或前面的数值不等于查找数，则证明当前数是第一个数值,否则第一个数值就在start------mid-1区间类
            if mid==0 or self._arr[mid-1]!=self._value: return mid
            return self.search_first_recursion(start, mid-1)
        elif self._arr[mid]>self._value:
            return self.search_first_recursion(start, mid-1)
        else:
            return self.search_first_recursion(mid+1, end)


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
    searchVal=45
    print('查找数值:'+str(searchVal))
    search=BinarySearch(4000)
    search.print_all()
    index=search._search(searchVal)
    if index==-1:
        print('未找到')
    else:
        print('找到，索引在'+str(index))
    index=search.search_first(searchVal)
    if index==-1:
        print('未找到第一个索引')
    else:
        print('找到，第一个索引在'+str(index))

    index=search.search_last(searchVal)
    if index==-1:
        print('未找到最后一个索引')
    else:
        print('找到，最后一个索引在'+str(index))

    index=search.search_greaterthan(searchVal)
    if index==-1:
        print('未找到第一个大于等于索引')
    else:
        print('找到，第一个大于等于索引在'+str(index))

    index=search.search_lessthan(searchVal)
    if index==-1:
        print('未找到最后一个小于等于索引')
    else:
        print('找到，最后一个小于等于索引在'+str(index))

if __name__=="__main__":
    test_BinarySearch()
