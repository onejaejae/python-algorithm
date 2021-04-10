import sys
import os

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

str = input()
stack = []
cnt = 0
for i in range(len(str)):
    if str[i] == ")":
        if str[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
    else:
        stack.append(str[i])

print(cnt)
