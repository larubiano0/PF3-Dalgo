import sys
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('{:f}'.format(end - start) + 's')
        return result
    return wrapper


def count_divisible_paths(m, k):
    k_multiples = 0
    dp = [[1] + [0] * m] + [[0] * (m + 1) for _ in range(m)]
    i = 0
    while k_multiples + k <= m:  
        for j in range(k_multiples + k, m + 1):  
            dp[i+1][j] = (dp[i][j - k] + dp[i+1][j - k]) % 998244353 
        k_multiples += k 
        k += 1  
        i += 1
    
    return sum([l[-1] for l in dp]) #% 998244353

@timer
def main():
    casos = int(sys.stdin.readline())
    for _ in range(casos):
        m, k = map(int, sys.stdin.readline().split())
        numero_de_caminos = count_divisible_paths(m, k)
        print(numero_de_caminos)


if __name__ == '__main__':
    main()
# python3.10 proyecto3.py < P0.in > P1.out
