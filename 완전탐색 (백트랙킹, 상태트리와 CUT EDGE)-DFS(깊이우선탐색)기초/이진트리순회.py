import sys
import os

sys.stdin = open("c: \workspaces\python\완전탐색(백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기

def DFS(v):
    if v > 7:
        return
    print(v)
    DFS(v*2)
    DFS(v*2+1)

DFS(1)
