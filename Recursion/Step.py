#台阶走法
#一次只能走1个台阶或2个台阶，共有多少种走法

def step(n:int)->int:
    if n==1:return 1
    if n==2:return 2
    
    return step(n-1)+step(n-2)

#斐波那契[Fibonacci]数列
def fibonacci(n:int)->int:
    if n==0:return 0
    if n==1:return 1
    
    return fibonacci(n-1)+fibonacci(n-2)

if __name__=="__main__":
    steps=step(9)
    print(steps)

    print(fibonacci(10))