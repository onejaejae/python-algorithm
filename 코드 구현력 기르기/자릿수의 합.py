import sys
import os

#sys.stdin = open("c:\workspaces\python\코드 구현력 기르기\input.txt", "rt")


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x//10
    return sum


'''
def digit_sum(x):
    sum = 0
   for x in str(x)
        sum += int(x)
    return sum
'''

n = int(input())
arr = list(map(int, input().split()))

max = 0
for x in arr:
    if(max < digit_sum(x)):
        max = digit_sum(x)

for x in arr:
    if(max == digit_sum(x)):
        print(x)
        break
