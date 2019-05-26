#二叉树
class Node:
    def __init__(self, data:int):
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self):
        self.head=None
    
    def print_all(self):
        p=self.head
        #前序遍历
        #self.previous_order(p)
        #中序遍历
        self.middle_order(p)
        #后序遍历
        #self.next_order(p)

    #前序遍历    
    def previous_order(self, node:Node):
        if not node: return
        print(node.data)
        #左子树
        self.previous_order(node.left)
        #右子树
        self.previous_order(node.right)

    #中序遍历
    def middle_order(self, node:Node):
        if not node:return
        self.middle_order(node.left)
        print(node.data)
        self.middle_order(node.right)
    
    #后序遍历
    def next_order(self, node:Node):
        if not node:return
        self.next_order(node.left)
        self.next_order(node.right)
        print(node.data)
    

    def insert(self, data:int):
        if not self.head:
            self.head=Node(data)
            return
        
        p=self.head
        while p:
            if data>p.data:
                if not p.right:
                    p.right=Node(data)
                    return
                p=p.right
            
            if data<p.data:
                if not p.left:
                    p.left=Node(data)
                    return
                p=p.left

            if data==p.data:
                return    

    def find(self, data:int)->Node:
        p=self.head
        while p:
            if p.data<data:
                p=p.right
            elif p.data>data:
                p=p.left
            else:
                return p
        return None

    def find_min(self)->Node:
        if not self.head: return None
        p=self.head
        while p.left:
            p=p.left
        return p

    def find_max(self)->Node:
        if not self.head: return None
        p=self.head
        while p.right:
            p=p.right
        return p

    def delete(self, data:int):
        p=self.head
        #查找删除节点
        prevNode=None
        while p and p.data!=data:
            prevNode=p
            if p.data<data:
                p=p.right
            else:
                p=p.left
        
        if not p:return
        
        #删除两个节点
        if p.left and p.right:
            minp=p.right
            minpParent=p #最小右节点父节点
            #查找最小节点
            while minp.left:
                minpParent=minp
                minp=minp.left
            p.data=minp.data
            p=minp              #用后绪删除代码进行删除
            prevNode=minpParent

        #删除节点是叶子节点或仅有一个节点
        child=None
        if p.left:child=p.left
        elif p.right:child=p.right
        else:child=None
        
        if not prevNode:self.head=child #删除的是根结点
        elif prevNode.left==p:prevNode.left=child   #删除左节点
        else:prevNode.right=child #删除右节点

def test_BinaryTree():
    print('初始化')
    binaryTree=BinaryTree()
    binaryTree.insert(10)
    binaryTree.insert(8)
    binaryTree.insert(13)
    binaryTree.insert(9)
    binaryTree.insert(4)
    binaryTree.insert(1)
    binaryTree.insert(3)
    binaryTree.insert(17)
    binaryTree.insert(15)
    binaryTree.print_all()

    print_find(binaryTree, 15)
    print_find(binaryTree, 66)
    node=binaryTree.find_min()
    print('最小值：'+str(node.data) if node else '未找到')

    node=binaryTree.find_max()
    print('最大值：'+str(node.data) if node else '未找到')

    print('删除节点:'+str(8))
    binaryTree.delete(8)
    binaryTree.print_all()

def print_find(binaryTree:BinaryTree, data:int):
    findNode=binaryTree.find(data)
    printStr='查找值:'+str(data)+',查找结果:'
    printStr+='找到' if findNode else '未找到'
    print(printStr)

if __name__=="__main__":
    test_BinaryTree()
