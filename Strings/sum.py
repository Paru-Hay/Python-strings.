# Given two strings denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2.
class Solution:
    def findSum(self, s1, s2):
        # Convert strings to integers, calculate the sum, and convert back to string.
        return str(int(s1) + int(s2))
    
# Example usage
s1 = "123"
s2 = "456"
solution = Solution()
print(solution.findSum(s1, s2))  