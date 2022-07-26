# 값을 받고 if 와 elif 또는 else로 마무리하며 처리하는 형식
#값을 받고 만들어둔 형식들로 대조해가며 값을 처리함

import sys

stack=[] 
 
N = int(sys.stdin.readline()) #갯수 받기

for i in range(N):
    a = sys.stdin.readline().split() #값받기
    
    order = a[0] #명령어 a[1]은 값
    
    if order == "push":
    	stack.append(int(a[1]))

    elif order == "pop":
        if len(stack) == 0: #stack안이 비어있다면
            print("-1")
        else:
            print(stack.pop())
    
    elif order == "size": 
        if not len(stack) == 0:
            print(len(stack))
        else:
            print("0")
            
    elif order == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    
    elif order == "top":
        if len(stack) == 0:
            print("-1")
        else: 
            print(stack[-1])
