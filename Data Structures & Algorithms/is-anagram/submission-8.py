class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram1 = {}
        anagram2 = {}

        for char in s:
            anagram1[char] = anagram1.get(char, 0) + 1

        for char in t:
            anagram2[char] = anagram2.get(char, 0) + 1
        
        if anagram1 == anagram2:
            return True
        else:
            return False

      