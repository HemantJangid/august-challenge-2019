for i in range(int(input())):
    n, k = map(int, input().split())
    if k == 1 or n%(k*k) == 0:
        print('NO')
    else:
        print('YES')


        