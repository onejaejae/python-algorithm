import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 중복을 제거하기 위해
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            sum = arr[i] + arr[j] + arr[m]
            res.add(sum)
new_res = sorted(res, reverse=True)
print(new_res[k-1])
