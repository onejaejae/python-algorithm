import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n = int(input())
max = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort(reverse=True)
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100

    # b==c를 a==b , a==c와 다르게 분기한 이유
    # b == c일 경우 b*100을 해야하기 때문이다.
    elif b == c:
        money = 1000 + b * 100
    else:
        money = a*100

    if money > max:
        max = money

print(max)
