class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths match (O(1))
        if len(s) != len(t):
            return False
        
       
        buckets = [0] * 26
        
         
        for i in range(len(s)):
            # Increment for string s, Decrement for string t 
            buckets[ord(s[i]) - ord('a')] += 1
            buckets[ord(t[i]) - ord('a')] -= 1
            
        
        for count in buckets:
            if count != 0:
                return False
                
        return True 