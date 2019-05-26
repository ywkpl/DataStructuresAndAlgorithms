#归并排序,分而治之
import random,time

class MergeSort:
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

        splitIndex=(start+end)//2
        self.sort_split(start, splitIndex)
        self.sort_split(splitIndex+1, end)

        self.merge_sort(start, splitIndex, end)

    def merge_sort(self, left:int, mid:int, right:int):
        marge=[]
        i,j=left,mid+1
        
        #比较搬移
        while i<=mid and j<=right:
            if(self._arr[i]<=self._arr[j]):
                marge.append(self._arr[i])
                i+=1
            else:
                marge.append(self._arr[j])
                j+=1
        
        #搬移剩余数据        
        while i<=mid:
            marge.append(self._arr[i])
            i+=1

        while j<=right:
            marge.append(self._arr[j])
            j+=1

        #复制
        i=0
        while i<len(marge):
            self._arr[left+i]=marge[i]
            i+=1    

    def sort(self):
        start=time.time()
        self.sort_split(0, len(self._arr)-1)
        end=time.time()
        print(end-start)

def test_MergeSort():
    print('初始化')
    sort=MergeSort(10000000)
    #sort.print_all()
    print('排序')
    sort.sort()
    #sort.print_all()

if __name__=="__main__":
    test_MergeSort()

