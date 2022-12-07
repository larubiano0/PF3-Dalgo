import sys


def count_divisible_paths(m, k):
    k_multiples = 0
    dp = [[1] + [0] * m]
    i = 0
    while k_multiples + k <= m:
        dp += [[0] * (m + 1)]
        for j in range(k_multiples + k, m + 1):
            dp[i + 1][j] = (dp[i][j - k] + dp[i + 1][j - k]) % 998244353
        k_multiples += k
        k += 1
        i += 1

    return sum([l[-1] for l in dp]) % 998244353


def main():
    casos = int(sys.stdin.readline())
    for _ in range(casos):
        try:
            m, k = map(int, sys.stdin.readline().split())
            numero_de_caminos = count_divisible_paths(m, k)
            print(numero_de_caminos)
        except:
            print(0)


if __name__ == '__main__':
    main()
# python3.10 proyecto3.py < P0.in > P1.out
