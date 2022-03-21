class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dist_steps(0, n, {})
    
    def dist_steps(self,current_stair, target_stair, memo):
        
        if current_stair == target_stair:
            return 1
        
        if current_stair > target_stair:
            return 0
        
        current_key = current_stair
        if current_key in memo:
            return memo[current_key]
        
        opt1 = self.dist_steps(current_stair+1, target_stair, memo)
        
        opt2 = self.dist_steps(current_stair+2, target_stair, memo)
        
        memo[current_key] = opt1+opt2
        
        return opt1+opt2
        