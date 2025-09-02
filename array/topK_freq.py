#  Solution 1 using python inbuilt sort method and hashmap or dict to store count of each num in array -> (O(nlogn))
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1

        print(freq)
        sorted_dict = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        print(sorted_dict)
            
        final_list = [i for i,k in sorted_dict[:k]]
        return final_list
    
# Solution 2 Using heap to sort(Hashmap + min heap (python only has min heap so i inputted negative count to get max count on top)) => O(n+Klogn)
from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1

        pq = [(-count, key) for key,count in freq.items()]
        print(pq)
        heapq.heapify(pq)
        print(pq)

        result = []
        for _ in range(k):
            count , val = heapq.heappop(pq)
            result.append(val)
        return result

# Solution 3 Using heap to sort(Hashmap + Priority Queue(length of heap == length of k)) for Best time complexity => O(nlogk)
from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1

        pq = []
        for key, count in freq.items():
            heapq.heappush(pq, (count,key))
            if len(pq) > k:
                heapq.heappop(pq)
        result = [num for count, num in pq]
        return result