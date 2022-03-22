class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res =  self.minimumCoinChange(0, amount, coins, {})
        if res == 100001:
            return -1
        
        return res
        
    def minimumCoinChange(self, current_index, amount, coins, memo):
        
        if amount == 0:
            return 0
        
        if current_index == len(coins):
            return 100001
        
        currentKey = str(current_index) + "-" + str(amount)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        considered = 100001
        
        if coins[current_index] <= amount:
            considered = 1 + self.minimumCoinChange(current_index, amount-coins[current_index], coins, memo)
            
        not_considered = self.minimumCoinChange(current_index+1, amount, coins, memo)
        
        memo[currentKey] = min(considered,not_considered)
        
        return memo[currentKey]
    
    
        
        