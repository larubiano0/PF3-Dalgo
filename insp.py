# Dynamic Programming function for counting the number of ways to reach a
# number m with divisible k steps
def count_divisible_paths(m, k):
    k_multiples = 0
    dp = [0] * (m + 1)  # dp[i] = number of paths to i
    dp[0] = 1  # base case
    ans = [0] * m  # ans[i] = number of paths to i with k steps
    while k_multiples + k <= m:  # It is not possible to reach a number greater than m
        aux_dp = [0] * (m + 1)  # new dp
        for i in range(k_multiples, m + 1 - k):  # loop over all paths to i
            aux_dp[i + k] = (dp[i] + aux_dp[i]) % 998244353  # add paths to i+k
            ans[i + k - 1] = (ans[i + k - 1] + aux_dp[i + k]
                              ) % 998244353  # add paths to i+k-1
        dp = aux_dp  # update dp
        k_multiples += k  # update multiple
        k += 1  # advance in the sequence
    print(ans[-1])  # print answer


#count_divisible_paths(10000, 7)
#count_divisible_paths(25252, 11)
#count_divisible_paths(200000, 1)
#count_divisible_paths(200000, 2)
count_divisible_paths(200000, 5)
count_divisible_paths(200000, 25)
count_divisible_paths(200000, 777)
count_divisible_paths(200000, 1337)
count_divisible_paths(200000, 200000)
