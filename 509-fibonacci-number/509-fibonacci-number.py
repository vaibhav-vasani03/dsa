class Solution:
    def fib(self, n: int) -> int:
        return self.fibonacci(n, {})
    
    def fibonacci(self, n, memo):
        if n==0:
            return 0
        
        if n==1:
            return 1
        
        current_key = n
        if current_key in memo:
            return memo[current_key]
        
        a = self.fibonacci(n-1, memo)
        b = self.fibonacci(n-2, memo)
        
        memo[current_key] = a+b
        
        return a+b
        