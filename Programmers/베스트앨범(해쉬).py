import sys
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(int)
    total_list = defaultdict(lambda: [])

    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        total_list[genres[i]].append((plays[i], i))

    genre_dict = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)

    for i in total_list:
        total_list[i] = sorted(total_list[i], key=lambda x: x[0], reverse=True)

    while len(genre_dict) > 0:
        genre_max = genre_dict.pop(0)

        for t in total_list:
            if t == genre_max[0]:
                if len(total_list[t]) > 1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))
