import sys
import os

sys.stdin = open(
    "c:\workspaces\python\탐색&시뮬레이션(string, 1차원, 2차원 리스트 탐색 )\input.txt", "rt")


def check(arr):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[arr[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


arr = [list(map(int, input().split())) for _ in range(9)]

if check(arr):
    print("YES")
else:
    print("NO")
