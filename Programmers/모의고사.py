def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if pattern1[idx % len(pattern1)] == answer:
            score[0] += 1
        if pattern2[idx % len(pattern2)] == answer:
            score[1] += 1
        if pattern3[idx % len(pattern3)] == answer:
            score[2] += 1

    for i, value in enumerate(score):
        if value == max(score):
            result.append(i+1)

    return result


solution([1, 3, 2, 4, 2])
