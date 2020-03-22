N = int(input("input: "))
for i in range(int(input("how many iterations would you like to compute?: "))):
    if N % 2 == 0:
        N = N // 2
    else:
        N = 3 * N + 1
    print(int(N))
