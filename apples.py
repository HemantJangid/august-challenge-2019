for i in range(int(input())):
    n, k = map(int, input().split())
    if k == 1 or n == k*k:
        print('NO')
    else:
        print('YES')