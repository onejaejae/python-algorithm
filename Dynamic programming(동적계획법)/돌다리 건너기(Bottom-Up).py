import sys

# sys.stdin = open(
#    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

# 개울을 건너는게 point, 개울을 건너야 하므로 한번 더 해야함

n = int(input())
arr = [0] * (n+2)

arr[1] = 1
arr[2] = 2

for i in range(2, n+1):
    arr[i+1] = arr[i] + arr[i-1]

print(arr[n+1])
