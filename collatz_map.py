def collatz(N):
    if N % 2 == 0:
        N = N / 2
    else:
        N = 3 * N + 1
