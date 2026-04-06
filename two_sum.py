class Solution:
    def two_sum_hashing(self,arr,target):
        mp={}
        for i,num in enumerate(arr):
            comp=target-num
            if comp in mp:
                return 'YES'
            mp[num]=i
        return "NO"
    def two_sum_2pointer(self,arr,target):
        sort_arr=sorted(arr) # sorted() --> Doesn't make changes to original array
        i,j=0,len(arr)-1
        while i<j:
            if sort_arr[i]+sort_arr[j] == target: return "YES"
            elif sort_arr[i]+sort_arr[j] < target: i+=1
            else: j-=1
        return "NO"
if __name__=="__main__":
    sol=Solution()
    arr=[2,3,4,6]
    target=11
    print(sol.two_sum_hashing(arr,target))
    print(sol.two_sum_2pointer(arr,target))
