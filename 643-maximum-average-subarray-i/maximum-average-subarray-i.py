class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
    # Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Return the average
        return max_sum / k