def solution(array, commands):
    answer = []

    for a, b, c in commands:
        result = []
        for i in range(a, b+1):
            result.append(array[i-1])
        result.sort()
        answer.append(result[c-1])

    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
