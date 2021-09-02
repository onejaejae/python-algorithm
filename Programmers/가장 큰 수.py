def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 0000을 input할 경우 0을 return해야하기 때문에
    # int 형변환 후 str로 형변환
    return str(int(''.join(numbers)))


solution([3, 30, 34, 5, 9])
