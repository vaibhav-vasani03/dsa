class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.coin_change(amount, coins, 0, {})
    
    def coin_change(self, amount, coins, current_index, memo):
        
        if amount == 0:
            return 1
        
        if current_index >= len(coins):
            return 0
        
        
        current_key = str(current_index) +"-"+str(amount)
        
        if current_key in memo:
            return memo[current_key]
        
        
        considered = 0
        if coins[current_index] <= amount:
            considered = self.coin_change(amount-coins[current_index], coins, current_index, memo)
            
        notconsidered = self.coin_change(amount, coins, current_index+1, memo)
        
        memo[current_key] = considered+notconsidered
        
        return memo[current_key]