class Solution:
    def tribonacci(self, n: int) -> int:
        return self.tribonacci_func(n, {})
    
    def tribonacci_func(self, n, memo):
        
        if n == 0:
            return 0
        
        if n in [1, 2]:
            return 1
        
        current_key = n
        
        if current_key in memo:
            return memo[current_key]
        
        num1 = self.tribonacci_func(n-1, memo)
        num2 = self.tribonacci_func(n-2, memo)
        num3 = self.tribonacci_func(n-3, memo)
        
        memo[current_key] = num1+num2+num3
        
        return num1+num2+num3
        