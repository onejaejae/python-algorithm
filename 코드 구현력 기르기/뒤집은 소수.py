import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res*10+t
        x = x//10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")
