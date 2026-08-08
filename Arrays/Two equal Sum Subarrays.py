class Solution:
    def canSplit(self, arr):
        n=len(arr)
        total=sum(arr)
        if total%2!=0:
            return False
        target=total//2
        prefixSum=0
        for i in range(n):
            prefixSum+=arr[i]
            if prefixSum==target:
                return True
        return False
        
