class Solution:
    def isValid(self, s: str) -> bool:
    
    # Map closing brackets to their matching opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
    
        for char in s:
            if char in mapping:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
    
        # If the stack is empty, all brackets were matched correctly
        return not stack