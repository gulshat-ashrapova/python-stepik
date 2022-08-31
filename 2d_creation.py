a = []
while True:
    s = input()

    if s == 'end':
        break
    a.append([int(i) for i in s.split()])


ans = [[0] * len(a[0]) for i in range(len(a))]
for i in range(len(a)):
    for j in range(len(a[0])):
        ans[i][j] = a[i-len(a)+1][j]+a[i-1][j]+a[i][j-len(a[0])+1]+a[i][j-1]

for i in ans:
    print(*i)



