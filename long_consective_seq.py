class Solution:
    def longest_consective_sequence(self,nums):
        #put all the values into map
        longest=1
        st=set()
        for i in nums:
            st.add(i)
        for i in nums:
            if i-1 not in st:
                cnt=1
                num=i
                while num+1 in st:
                    cnt+=1
                    num=num+1
            longest=max(longest,cnt)
        return longest

if __name__=="__main__":
    sol=Solution()
    nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longest_consective_sequence(nums))