import sys

list=[] #스택

def push(a): #스택 넣기
  list.append(a)

def pop(): #스택 빼기
  if list:
    pop(list)
  else:
    print("-1")

def size(): #스택 안 갯수
  print(len(list))

def empty(): #스택이 비어있다면 -1 있다면 1을
  if not list:
    print("1")
  else:
    print("-1")

def top(): #스택이 비어있으면 -1을 아니면 가장 위에있는 값을
  if not list:
    print("-1")
  else:
    print(list[-1])
    
N=int(sys.stdin.readline().rstrip())
