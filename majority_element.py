class Solution:
    def majority_element(self,nums):
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        for key,value in mp.items():
            if value> len(nums)//2:
                return key
            
        return -1
    def majority_element_2(self,nums):
        contestant=0
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                contestant=nums[i]
                cnt=1
            elif contestant==nums[i]:
                cnt+=1
            else:
                cnt-=1
        cnt1=nums.count(contestant) 
        print(cnt1,cnt)
        if cnt1>len(nums)//2:
            return contestant
        return -1


if __name__=="__main__":
    sol=Solution()
    nums=[5,5,5,10,2]
    print(sol.majority_element_2(nums))