import sys
import os

sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

sum = 0
j = 0

for x in arr:
    if x == 0:
        j = 0
        continue

    j += 1
    sum += j

print(sum)
