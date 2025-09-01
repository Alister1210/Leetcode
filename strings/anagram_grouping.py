# Solution 1
# In the below soln we use sorting characters method to sort the characters and append the words in same key if the sorted words are equal in dictionary
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_grps = {}

        for word in strs:
            key = "".join(sorted(word)) # we sort word in new list using sorted [a,e,t] => join them to get 'aet'
            print(key, sorted(word)) # eg. aet ['a', 'e', 't']
            if key not in anagram_grps:
                anagram_grps[key] = []
            anagram_grps[key].append(word)

        print(anagram_grps) # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        final_list = list(anagram_grps.values())
        print(final_list) #[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        return final_list
        
# Solution 2 (Optimal solution) uses char freq counting method