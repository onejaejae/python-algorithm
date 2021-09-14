def solution(name):
    answer = 0

    for x in name:
        if x > "N":
            answer += (91 - ord(x))
        else:
            answer += (ord(x) - 65)

    for i in range(1, len(name) - 1):
        if name[i] != "A":
            break
    else:
        print(answer + 1)
        return answer + 1

    print(answer + len(name) - 1)
    return answer + len(name) - 1


solution("JAN")
