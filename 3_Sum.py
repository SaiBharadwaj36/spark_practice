class Solution:
    def three_sum(self,nums):
        ans=set()
        n=len(nums)
        for i in range(n):
            hashSet=set()
            for j in range(i,n):
                required=-(nums[i]+nums[j])
                if required in hashSet:
                    tu=tuple(sorted([nums[i],nums[j],required]))
                    ans.add(tu)
                hashSet.add(nums[j])
        return [list(tup) for tup in ans]
    
    def three_sum_v2(self,nums):
        # sort the array
        # pick a number with for loop
        # then use the two pointer algo to find the other three numbers
        nums.sort()
        ans=set()
        n=len(nums)
        for k in range(n):
            target=nums[k]
            i,j=0,n-1
            while i<j:
                if -(nums[i]+nums[j])==target:
                    ans.add(tuple(sorted([nums[i],nums[j],target])))
                    i+=1
                    j-=1
                elif nums[i]+nums[j]<target:
                    i+=1
                else: j-=1
        return [list(tup) for tup in ans]



if __name__=="__main__":
    sol=Solution()
    nums=[-1, 0, 1, 2, -1, -4]
    print(sol.three_sum_v2(nums))
        
