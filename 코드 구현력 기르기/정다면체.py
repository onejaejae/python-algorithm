import sys
import os

sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n, m = map(int, input().split())

cnt = [0]*(m+n+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

max = cnt[0]
for i in range(1, len(cnt)):
    if cnt[i] > max:
        max = cnt[i]
for i in range(len(cnt)):
    if max == cnt[i]:
        print(i, end=' ')
