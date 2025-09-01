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

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_grps = {}

        for string in sorted(strs):
            char_count = [0]*26
            for s in string:
                char_count[ord(s) - ord('a')] +=1
            key = tuple(char_count) #list cannot be used as keys
            if key not in anagram_grps:
                anagram_grps[key] = []
            anagram_grps[key].append(string)

        final_list = list(anagram_grps.values())
        return final_list
        
# Solution 3 using defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_grps = defaultdict(list)

        for string in sorted(strs):
            char_count = [0]*26
            for i in string:
                char_count[ord(i) - ord('a')] +=1

            anagram_grps[tuple(char_count)].append(string)

        return anagram_grps.values()