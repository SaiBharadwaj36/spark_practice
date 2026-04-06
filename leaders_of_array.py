class Solution:
    def leaders_of_array(self,nums):
        n=len(nums)
        max_ele=float('-inf')
        leaders=[]
        for i in range(n-1,-1,-1):
            if nums[i]>max_ele:
                max_ele=nums[i]
                leaders.append(max_ele)
        leaders.reverse()
        return leaders
    
if __name__=='__main__':
    sol=Solution()
    nums=[4, 7, 1, 0]
    print(sol.leaders_of_array(nums))

                
