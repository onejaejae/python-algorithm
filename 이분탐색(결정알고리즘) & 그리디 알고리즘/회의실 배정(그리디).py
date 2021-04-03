import sys
import os

# sys.stdin = open(
#    "c:\workspaces\python\이분탐색(결정알고리즘) & 그리디 알고리즘\input.txt", "rt")

n = int(input())
arr = []

for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort(key=lambda x: (x[1], x[0]))

end = arr[0][1]
cnt = 1
for i in range(1, n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)
