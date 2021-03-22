import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")

n = int(input())

for i in range(n):
    arr = input()
    mid = len(arr) // 2
    size = len(arr)

    # s[::-1] => s를 reverse해준다
    # if s == s[::-1]로 구현하면 훨씬 파이썬스럽게 가능

    for j in range(mid):
        # python은 index를 - 로 접근할 수 있다.
        # arr[-1] = arr의 마지막 인덱스
        # if arr[j].lower() != arr[-1 - j].lower():
        if arr[j].lower() != arr[size - 1 - j].lower():
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))
