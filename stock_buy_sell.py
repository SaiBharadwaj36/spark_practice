#buy on low price day and sell on high price day to get maximum profit
class Solution:
    def stock_buy_sell_profit(self,nums):
        maxi_profit=0
        buy=float('inf')
        for i in nums:
            buy=min(buy,i)
            maxi_profit=max(maxi_profit,i-buy)
        return maxi_profit
    
if __name__=='__main__':
    sol=Solution()
    nums=[7,6,4,3,1]
    print(sol.stock_buy_sell_profit(nums))
