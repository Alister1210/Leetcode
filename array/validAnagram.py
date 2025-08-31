# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(self, s, t):
        charCounter = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            charCounter[ord(s[i]) - ord('a')] +=1
            charCounter[ord(t[i]) - ord('a')] -=1
        for count in charCounter:
            if count != 0:
                return False
        return True