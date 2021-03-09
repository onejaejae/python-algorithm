import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
ave = round(sum(arr)/n)
res = 0
min = float('inf')
for idx, x in enumerate(arr):
    tmp = abs(ave - x)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if(score < x):
            # min은 같으므로 안바꿔도 됨
            score = x
            res = idx+1

print(ave, res)
