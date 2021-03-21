
import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")

str = input()
res = 0

for x in str:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
