class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}

        for i in s:
            s_letters[i] = s_letters.get(i, 0) + 1

        for i in t:
            t_letters[i] = t_letters.get(i, 0) + 1
            
        return s_letters == t_letters