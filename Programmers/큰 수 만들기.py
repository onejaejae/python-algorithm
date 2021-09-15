def solution(number, k):

    stack = []

    for i in number:
        while stack and i > stack[-1] and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)

    return "".join(stack[:len(stack)-k])


solution("999", 1)
