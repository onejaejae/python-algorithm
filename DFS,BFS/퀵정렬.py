import sys
import os

sys.stdin = open("c:\workspaces\python\DFS,BFS\input.txt", "rt")


def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                tmp = arr[pos]
                arr[pos] = arr[i]
                arr[i] = tmp
                pos += 1
        tmp = arr[pos]
        arr[pos] = arr[rt]
        arr[rt] = tmp

        Qsort(lt, pos-1)
        Qsort(pos+1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 35, 15, 67, 11, 60, 20, 23]
    print("Before sort: ", end=" ")
    print(arr)
    Qsort(0, 9)
    print("After sort: ", end=" ")
    print(arr)
