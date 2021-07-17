import sys
import collections

sys.stdin = open(
    "c:\workspaces\python\Programmers\input.txt", "rt")


# 정렬을 이용하면 바로 뒤의 숫자가 앞 숫자의 접두어가 안되면 그 뒤는 확인할 필요가 없다

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) > len(phone_book[i+1]):
            continue

        tmp1 = phone_book[i]
        tmp2 = phone_book[i+1]

        for i in range(len(tmp1)):
            if tmp1[i] != tmp2[i]:
                break
        else:
            answer = False

    return answer


print(solution(["12", "123", "1235", "567", "88"]))
