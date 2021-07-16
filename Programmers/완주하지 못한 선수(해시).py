import sys
import collections

sys.stdin = open(
    "c:\workspaces\python\Programmers\input.txt", "rt")


def solution(participant, completion):

    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]


solution(["mislav", "stanko", "mislav", "ana"],
         ["stanko", "ana", "mislav"])
