class Solution:
    def majority_ele_2(self,nums):
        n=len(nums)
        el1=float('inf')
        el2=float('inf')
        cnt1,cnt2=0,0
        mini=n//3+1
        for i in range(n):
            if cnt1==0 and nums[i]!=el2:
                el1=nums[i]
                cnt1+=1
            if cnt2==0 and nums[i]!=el1:
                el2=nums[i]
                cnt2+=1
            elif nums[i]==el1: cnt1+=1
            elif nums[i]==el2: cnt2+=1
            else:
                cnt1-=1
                cnt2=-1
            
        count1=nums.count(el1)
        count2=nums.count(el2)
        ans=[]
        if count1>=mini:
            ans.append(el1)
        if count2>=mini and el1!=el2:
            ans.append(el2)
        return ans

if __name__=="__main__":
    sol=Solution()
    nums=[11, 33, 33, 11, 33, 11]
    print(sol.majority_ele_2(nums))