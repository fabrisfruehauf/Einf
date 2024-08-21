p=[0,1,1,3,5,5,7,9,8,10,10]

def best_price (n):
    best = p[n]
    for i in range(n):
        b = best_price (n-1)
        if p[i] + b > best:
            best = p[i]+b
            return best


