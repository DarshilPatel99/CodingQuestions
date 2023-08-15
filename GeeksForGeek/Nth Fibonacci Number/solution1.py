class Solution:
    def solve(self, n, dp):
        if n <= 2:
            return 1
        if dp[n] == 0:
            dp[n] = (self.solve(n-1, dp) + self.solve(n-2, dp))%(1000000007)
        return dp[n]
            
    def nthFibonacci(self, n):
        dp = [0]*(n+1)
        return self.solve(n, dp)

solution = Solution()
print(solution.nthFibonacci(10))