class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = {}

        heap = []

        for num in nums:
            buckets[num] = buckets.get(num, 0) + 1

        print(list(buckets.items()))
        
        for num, freq in buckets.items():
            heapq.heappush(heap, (-freq, num))
        
        print(heap)

        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res        
