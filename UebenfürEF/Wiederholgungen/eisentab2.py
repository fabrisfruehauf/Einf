p = [0, 1, 1, 3, 5, 5, 7, 9, 8, 10, 10]


def best_price(n):

    dp = [0] * (n + 1)


    for i in range(1, n + 1):
        best = p[i]
        for j in range(1, i):
            best = max(best, p[j] + dp[i - j])
        dp[i] = best


    return dp[n]



n = 10
print(f"Der beste Preis für eine Länge von {n} ist: {best_price(n)}")
