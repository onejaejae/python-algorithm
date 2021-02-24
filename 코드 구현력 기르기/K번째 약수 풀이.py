N, K = map(int, input().split())
cnt = 0
for n in range(1, N+1):
    if N % n == 0:
        cnt += 1
    if cnt == K:
        print(n)
        break
else:
    print(-1)
