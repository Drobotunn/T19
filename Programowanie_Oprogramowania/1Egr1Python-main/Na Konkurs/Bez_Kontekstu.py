n, m = map(int, input().split())
wypowiedz = input()
fragment = input()

F = [0] * 200
for i in range(m):
    F[ord(fragment[i])] += 1

for j in range(n - m + 1):
    W = [0] * 200
    for k in range(m):
        F[ord(wypowiedz[k + j])] += 1
