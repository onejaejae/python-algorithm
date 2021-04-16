import sys
import os

sys.stdin = open("c:\workspaces\python\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for _ in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
