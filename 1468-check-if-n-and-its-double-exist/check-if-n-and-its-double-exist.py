class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
       
        seen = set()
        
        for x in arr:
            # Check if the double or the half exists in our set
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            # Add current number to the set for future comparisons
            seen.add(x)
            
        return False