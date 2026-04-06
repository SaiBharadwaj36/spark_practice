import math 
class Solution:
    def calculateHours(self,nums,min_bananas):
        maxHours=0
        for i in nums:
            maxHours+=math.ceil(i/min_bananas)
        return maxHours
    def koko_eating_banana(self,nums,h):
        # we need to find the minimum eating speed
        maxi=max(nums)
        for i in range(1,maxi+1):
            hours=self.calculateHours(nums,i)

            if hours<=h:
                return i
        return maxi
    def binary_search_v(self,nums,h):
        maxi=max(nums)
        low,high=1,maxi
        ans=maxi
        while low<=high:
            mid=(low+high)//2
            totalH=self.calculateHours(nums,mid)
            if totalH<=h:
                ans=mid
                high=mid-1
            else: low=mid+1
        return ans

if __name__=='__main__':
    sol=Solution()
    nums=[7, 15, 6, 3]
    h=8
    print(sol.binary_search_v(nums,h))