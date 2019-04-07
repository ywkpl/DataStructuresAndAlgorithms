class Node:
    def __init__(self, data:int, next=None):
        self.data=data
        self._next=next

class SingleLoop(object):
    """单循环链表"""
    def __init__(self):
        self._head=None
        self._len=0

    def insert_node_to_head(self, node:Node):
        node._next=self._head
        self._head=node
        node._next=self._head
        self._len+=1

    def insert_value_to_head(self, value:int):
        newNode=Node(value)
        if not self._head:
            self.insert_first_node(newNode)
            return
        
        newNode._next=self._head
        #移至尾部指向新結點
        node=self.get_last_node()
        node._next=newNode

        self._head=newNode
        self._len+=1

    def append_value(self, value:int):
        newNode=Node(value)
        if not self._head:
            self.insert_first_node(newNode)
            return

        newNode._next=self._head
        #移至鏈尾並添加節點
        node=self.get_last_node()
        node._next=newNode
        self._len+=1

    def get_last_node(self)->Node:
        node=self._head
        while node and node._next!=self._head:
            node=node._next
        return node

    def insert_first_node(self, node:Node):
        self._head=node
        node._next=self._head
        self._len+=1

    # def delete_by_node(self, node:Node):
    #     if not node or not self._head:
    #         return
        
    #     cur, prev=self._head, None
    #     while cur and cur!=node:
    #         prev=cur
    #         cur=cur._next

    #     if not prev:        #首节点
    #         self._head=None
    #         cur=None
    #         return

    #     if cur==self._head:  #首节点
    #         if self._head._next:
    #             self._head=self._head._next
    #     prev._next=cur._next
        


        

    def len(self)->int:
        return self._len

    def __iter__(self):
        node=self._head
        while node and node._next!=self._head:
            yield node.data
            node=node._next
    
    def print_all(self):
        if not self._head: return
        node=self._head
        while node and node._next!=self._head:
            print(node.data)
            node=node._next
        print(node.data)

    

def Josephus(personCount:int):
    link=SingleLoop()
    for i in range(1,personCount):
        link.append_value(i)
    
    #定位prev指针
    cur=link._head
    while cur and cur._next!=link._head:
        cur=cur._next
    prev=cur
    
    #删除节点
    i=1
    cur=link._head
    while cur and link._len>2:
        if i%3==0:
            if cur==link._head:
                link._head=cur._next
            prev._next=cur._next
            link._len-=1

        prev=cur
        cur=cur._next
        i=i+1
        
    link.print_all()

def test_SingleLoopLinkedList():
    link=SingleLoop()
    link.append_value(31)
    link.append_value(30)
    link.append_value(29)
    assert link.len==3
    link.print_all()
    

    print('约瑟夫问题：')
    Josephus(42)

if __name__=="__main__":
    test_SingleLoopLinkedList()