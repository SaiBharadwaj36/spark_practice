class Solution:
    def max_subarray_sum(self,nums):
        maxi=float('-inf')
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0

        return maxi
    def max_subarray_sum_indices(self,nums):
        maxi=float('-inf')
        sum=0
        st=0
        end=-1
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
                end=i
            if sum<0:
                sum=0
                st=i+1

        return (st,end)
if __name__=="__main__":
    sol=Solution()
    nums=[ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
    print(sol.max_subarray_sum(nums))
    print(sol.max_subarray_sum_indices(nums))
