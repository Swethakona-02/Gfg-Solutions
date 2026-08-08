class Solution:
    def findDuplicates(self, arr):
        s=set()
        ans=[]
        for num in arr:
            if num in s:
                ans.append(num)
            else:
                s.add(num)
        return ans
