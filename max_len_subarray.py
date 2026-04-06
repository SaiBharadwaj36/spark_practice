# find the max length of the subarray with sum zero.
class Solution:
    def max_len_SubarrayWithZeroSum(self,nums):
        mp={}
        max_len=0
        sum=0
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            if sum==0:
                max_len=i+1
            else :
                if sum in mp:
                    max_len=max(max_len,i-mp[sum])
                else: mp[sum]=i
        return max_len

if __name__=='__main__':
    sol=Solution()
    nums=[9, -3, 3, -1, 6, -5]
    print(sol.max_len_SubarrayWithZeroSum(nums))