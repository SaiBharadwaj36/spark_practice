class Solution:
    def subarray_count_target(self,nums,k):
        mp={}
        prefixSum=0
        count=0
        mp[0]=1
        for i in nums:
            prefixSum+=i
            remove=prefixSum-k
            if remove in mp:
                count+=mp[remove]
            
            mp[prefixSum]=mp.get(prefixSum,0)+1
        return count
if __name__=="__main__":
    sol=Solution()
    nums=[3, 1, 2, 4]
    k=6
    print(sol.subarray_count_target(nums,k))
