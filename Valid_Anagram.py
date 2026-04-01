class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count characters using dictionary
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True

s = "anagram"
t = "nagaram"
obj=Solution()
obj.isAnagram(s, t)
        
        