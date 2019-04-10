from typing import Optional

class Node:
    def __init__(self, data:int, next=None):
        self.data=data
        self._next=next

class SingleLinkedList:
    def __init__(self):
        self._head=None
        self.__len=0

    def insert_node_to_head(self, node:Node):
        node._next=self._head
        self._head=node
        self.__len+=1

    def insert_value_to_head(self, value:int):
        newNode=Node(value)
        self.insert_node_to_head(newNode)

    def insert_value_before(self, value:int, searchValue:int):
        if self._head.data==searchValue:
            self.insert_value_to_head(value)
            return

        newNode=Node(value)
        cur, prev=self._head._next, self._head
        while cur and cur.data!=searchValue:
            prev=cur
            cur=cur._next
        
        if cur:
            newNode._next=cur
            prev._next=newNode
            self.__len+=1

    def insert_value_after(self, value:int, searchValue:int):
        cur=self._head
        while cur and cur.data!=searchValue:
            cur=cur._next

        if cur:
            newNode=Node(value)
            if cur._next:
                newNode._next=cur._next
            cur._next=newNode
            self.__len+=1

    def insert_node_after(self, value:int, node:Node):
        if not node or not node.data:
            return
        self.insert_value_after(value, node.data)

    def delete_by_value(self, value:int):
        if not self._head or not value:
            return
        cur, prev=self._head, None
        
        while cur and cur.data!=value:
            prev=cur
            cur=cur._next

        if prev and prev._next:
            prev._next=cur._next

        if not prev:
            self._head=self._head._next if self._head._next else None
        
        if cur:
            cur=None
            self.__len-=1
            
    def len(self)->int:
        return self.__len

    def __iter__(self):
        node=self._head
        while node:
            yield node.data
            node=node._next
    
    def print_all(self):
        for item in self:
            print(item)

    def find_by_value(self, value:int)->Optional[Node]:
        p=self._head
        while p and not p.data==value:
            p=p._next
        return p

    def find_by_index(self, index:int)->Optional[Node]:
        p=self._head
        position=0
        while p and position!=index:
            position+=1
            p=p._next
        return p

    #另建链表方式
    def reverse(self):
        if not self._head:
            return
        
        virtualHead, cur, remove=None, self._head, None
        while cur:
            remove=cur
            cur=cur._next
            #搬移
            remove._next=virtualHead
            virtualHead=remove

        self._head=virtualHead

    #交换方式[原地交換,head指針不新建]
    def reverse_location_change(self):
        if not self._head or not self._head._next:
            return
        prev, next=self._head, self._head._next
        while next:
            prev._next=next._next
            next._next=self._head
            self._head=next
            next=prev._next
        

    #反转到指定节点
    def reverse_until_node(self, node:Node):
        if not self._head or not self._head._next or self._head==node:
            return
        
        prev, next=self._head, self._head._next
        while next and next!=node:
            prev._next=next._next
            next._next=self._head
            self._head=next
            next=prev._next

    #查找中间节点长度法
    def find_middle_node_length(self)->Optional[Node]:
        if not self._head or self.__len==1:
            return self._head
        middleIndex=(self.__len-1)//2
        return self.find_by_index(middleIndex)

    #查找中间节点    
    def find_middle_node(self)->Optional[Node]:
        if not self._head:
            return self._head

        p,q=self._head, self._head
        while q._next and q._next._next:
            p=p._next
            q=q._next._next

        return p

    #回文判断
    def IsPalindromic(self)->bool:
        if not self._head:return False
        if not self._head._next:return True
        
        #查找中间节点
        p,q=self._head, self._head
        while q._next and q._next._next:
            p=p._next
            q=q._next._next
        
        #q._next=null 为奇数，p位于中间位置，否则为偶数，下移一位
        reverseNode=p if not q._next else p._next
        q=p._next
        #反转至reverseNode节点
        self.reverse_until_node(reverseNode)
        p=self._head
        while q:
            if p.data!=q.data:
                return False
            p=p._next
            q=q._next

        return True

    def LRUCache(self, value:int):
        cacheNode=Node(value)
        if not self._head:
            self._head=cacheNode
            return

        if self._head.data==value:
            return
        
        cur,prev=self._head,None
        #遍曆現有鏈表
        while cur and cur.data!=value:
            prev=cur
            cur=cur._next
            
        #在鏈表中    
        if cur:
            prev._next=cur._next
            cur._next=self._head
            self._head=cur
            return

        #統計數量[可用len]
        i=1
        cur,prev=self._head,None
        while cur and cur._next:
            i+=1
            prev=cur
            cur=cur._next

        #鏈表滿
        if i==5:
            prev._next=None
            self.__len-=1
        
        cacheNode._next=self._head
        self._head=cacheNode

def test_singleLinkedList():
    link=SingleLinkedList()
    link.insert_value_to_head(24)
    link.insert_node_to_head(Node(33))
    link.insert_value_to_head(56)
    assert link.len()==3

    findNode=link.find_by_value(24)
    assert findNode is not None

    findNode=link.find_by_index(2)
    assert findNode.data==24

    link.delete_by_value(33)

    link.insert_value_before(88, 24)
    link.insert_value_before(77, 56)
    link.insert_value_before(1, 88)
    
    link.insert_value_after(45, 77)
    link.insert_value_after(40, 56)
    link.insert_value_after(100, 24)
    link.insert_value_after(5, 24)
    link.insert_value_after(456, 24)
    link.print_all()


    print('反转链表')
    link.reverse()
    link.print_all()

    print('另一种反转:')
    link.reverse_location_change()
    link.print_all()

    findNode=link.find_by_value(456)
    print('反转到结点:'+str(findNode.data))
    link.reverse_until_node(findNode)
    link.print_all()

    print('查找中间节点：')
    findNode=link.find_middle_node()
    print(findNode.data)

    print('查找中间节点长度法：')
    findNode=link.find_middle_node_length()
    print(findNode.data)

    print('新建回文链表：')
    linkPalindromic=SingleLinkedList()
    linkPalindromic.insert_value_to_head(5)
    linkPalindromic.insert_value_to_head(4)
    linkPalindromic.insert_value_to_head(3)
    linkPalindromic.insert_value_to_head(3)
    linkPalindromic.insert_value_to_head(4)
    linkPalindromic.insert_value_to_head(5)

    linkPalindromic.print_all()
    isPalindromic= linkPalindromic.IsPalindromic()
    print('判断回文结果：'+str(isPalindromic))

    print('新建LRU(最近最少使用策略)链表,依次緩存3,4, 5, 10, 10, 9：')
    LRULink=SingleLinkedList()
    LRULink.LRUCache(3)
    LRULink.LRUCache(4)
    LRULink.LRUCache(5)
    LRULink.LRUCache(10)
    LRULink.LRUCache(10)
    LRULink.LRUCache(9)

    LRULink.print_all()
    print('缓存：'+str(8))
    LRULink.LRUCache(8)
    LRULink.print_all()
    print('缓存：'+str(10))
    LRULink.LRUCache(10)
    LRULink.print_all()
    print('缓存：'+str(3))
    LRULink.LRUCache(3)
    LRULink.print_all()
    print('缓存：'+str(7))
    LRULink.LRUCache(7)

    LRULink.print_all()
if __name__=="__main__":
    test_singleLinkedList()
    
    