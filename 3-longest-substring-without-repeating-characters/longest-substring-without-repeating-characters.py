class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        left = 0
        max_length = 0
        
        # 'right' pointer expands the window
        for right in range(len(s)):
            # While we have a duplicate, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the new unique character and calculate window size
            char_set.add(s[right])
            # Window size is (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length