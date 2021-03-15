import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n = int(input())
arr = [0] * (n+1)


count = 0
for i in range(2, n+1):
    if arr[i] == 0:
        count += 1
        # for문 range의 세번째 option은 step을 나타냄   
        for j in range(i*2, n+1, i):
            if j % i == 0:
                arr[j] = 1

print(count)
