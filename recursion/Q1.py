def minDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a 2D matrix to store the minimum ASCII sum at each position
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and first column of the matrix
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])
    
    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # Characters are equal, no deletion needed
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),   # Delete s1[i-1]
                               dp[i][j-1] + ord(s2[j-1]))   # Delete s2[j-1]
    
    return dp[m][n]

s1 = "sea"
s2 = "eat"
print(minDeleteSum(s1, s2)) 
