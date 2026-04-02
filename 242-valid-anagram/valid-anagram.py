class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths match (O(1))
        
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Count characters in string s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Subtract counts using string t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True