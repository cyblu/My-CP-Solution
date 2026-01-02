N, M = map(int, input().split())
matriks = []

for i in range(N):
    matriks.append(list(map(int, input().split())))

for j in range(M):
    for i in range(N-1, -1, -1):
        print(matriks[i][j], end=' ')
    print()
