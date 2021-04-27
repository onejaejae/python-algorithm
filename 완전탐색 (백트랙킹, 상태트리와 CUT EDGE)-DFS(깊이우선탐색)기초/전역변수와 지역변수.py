def DFS1():
    cnt = 3
    print(cnt)


def DFS2():
    global cnt
    if cnt == 5:
        cnt = cnt + 1
        print(cntg)


if __name__ == "__main__":
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)
