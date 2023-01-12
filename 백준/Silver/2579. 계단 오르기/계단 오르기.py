n = int(input())

ab = []
for i in range(n):
    ab.append(int(input()))

dp = [0 for i in range(n)]

dp[0] = ab[0]
if n >= 2:
    dp[1] = ab[1]+ab[0]
    if n >= 3:
        dp[2] = max(ab[2]+ab[0] , ab[2]+ab[1])

for i in range(3,n):
    value1 = ab[i] + ab[i-1] + dp[i-3]
    value2 = ab[i] + dp[i-2]
    dp[i] = max(value1,value2)

print(dp[n-1])