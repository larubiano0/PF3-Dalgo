import sys
from math import ceil


def count_divisible_paths(m, k):
    k_multiples = 0
    dp = [[1] + [0] * m]
    numero_de_caminos = 0
    for i in range(1, ceil(1 / 2 * (8 * m + 1)**0.5 - 1 / 2)):
        dp += [[0] * (m + 1)]
        for j in range(k_multiples + k, m + 1):
            dp[i][j] = (dp[i - 1][j - k] + dp[i][j - k]) % 998244353
        numero_de_caminos = (numero_de_caminos + dp[i][-1]) % 998244353
        k_multiples += k
        k += 1

    return numero_de_caminos


def main():
    casos = int(sys.stdin.readline())
    for _ in range(casos):
        try:
            m, k = map(int, sys.stdin.readline().split())
            numero_de_caminos = count_divisible_paths(m, k)
            print(numero_de_caminos)
        except BaseException:
            print(0)


if __name__ == '__main__':
    main()
# python3.10 proyecto3.py < P0.in > P1.out
