import sys
from collections import Counter

#(의상종류 별 의상 수 + 1)씩 모두 곱하는 이유는 의상종류 별 의상수에 그 의상을 안 입는 경우의 수도 곱하는 것입니다.
# 거기에 추가적으로 -1을 하는 이유는 아무것도 모두 안 입는 경우의 수를 빼는 것입니다.

sys.stdin = open(
    "c:\workspaces\python\Programmers\input.txt", "rt")


def solution(clothes):
    values = []
    for i in range(len(clothes)):
        values.append(clothes[i][1])

    result = (Counter(values))
    answer = 1
    for key, value in result.items():
        answer *= value + 1

    answer -= 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses",
                                            "eyewear"], ["green_turban", "headgear"]]))
