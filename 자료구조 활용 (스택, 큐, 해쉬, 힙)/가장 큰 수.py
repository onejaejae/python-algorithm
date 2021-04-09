import sys
import os

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m > 0:
    stack = stack[:-m]

for x in stack:
    print(x, end="")
