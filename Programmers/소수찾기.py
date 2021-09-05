from itertools import permutations

# |=, &=, -=, ^= : = 과 조합함으로써 연산과 동시에 할당합니다.


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))

    a -= set(range(0, 2))

    # int(max(a) ** 0.5): 가장 큰 수의 제곱근
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


solution("123")
