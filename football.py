for i in range(int(input())):
    n = int(input())
    max = 0
    a = [int(x) for x in input().split()]
    b = list(map(int, input().split()))
    for j in range(n):
        num = a[j]*20 - b[j]*10
        if num > max:
            max = num

    print(max)

