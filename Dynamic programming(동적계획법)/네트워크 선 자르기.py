import sys
import os

sys.stdin = open(
    "c:\workspaces\python\Dynamic programming(동적계획법)\input.txt", "rt")

n = int(input())
arr = [0] * n

arr[0] = 1
arr[1] = 2

for i in range(2, n):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n-1])
