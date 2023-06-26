def arrageCoins(n):
    k = 0

    while n >= k+1:
         
         k += 1
         n -= k
    
    return k

n1 = 9
print(arrageCoins(n1))