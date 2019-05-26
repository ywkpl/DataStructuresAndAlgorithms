#红黑树

class Node:
    def __init__(self, data:int):
        self.data=data
        self.left=None
        self.right=None

class RedBlackTree:
    def __init__(self):
        self.head=None

    def print_all(self):
        self.middle_order(self.head)

    def middle_order(self, node:node):
        if not node:
            return

        self.middle_order(node.left)
        print(node.data)
        self.middle_order(node.right)

    def insert(self, data:int):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        
        p=self.head
        while p:
            if data>p.data:
                if not p.right:
                    p.right=newNode
                    return
                p=p.right
            elif data<p.data:
                if not p.left:
                    p.left=newNode
                    return
                p=p.left
            else:
                if p.right:
                    if p.right.data==data:
                        p=p.right
                    else:
                         newNode.right=p.right
                         p.right=newNode
                         return
                else:
                    p.right=newNode
                    return

    def delete(self, data:int):
        if not self.head: return
        p=self.head
        #查找删除节点
        prevNode=None
        while p and p.data!=data:
            prevNode=p
            if p.data<data:
                p=p.right
            else:
                p=p.left
        
        if not p: return
        
        
        
