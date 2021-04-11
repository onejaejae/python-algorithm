import sys
import os

#sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

str = input()
postfix = []
stack = []
res = ""

for x in str:
    if 48 <= ord(x) <= 57:
        postfix.append(x)
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                postfix.append(stack.pop())
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
while stack:
    postfix.append(stack.pop())

for x in postfix:
    print(x, end="")
