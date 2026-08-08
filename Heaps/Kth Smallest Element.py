import heapq
class Solution:
    def kthSmallest(self, arr, k):W
        heap=[]
        n=len(arr)
        for ind in range(0,k):
            heapq.heappush(heap,-arr[ind])
        for ind in range(k,n):
            if(-arr[ind]>heap[0]):
                heapq.heappop(heap)
                (heapq.heappush(heap,-arr[ind]))
        return (-heap[0])
