import sys
import os

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

postfix = input()
stack = []

for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif x == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif x == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif x == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
print(stack[-1])
