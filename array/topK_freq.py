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
    
