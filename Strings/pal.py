# This checks if the given string is palindrome or not.
def isPalindrome(s):
    return s == s[::-1]


# Example usage
s = "madam"
print(isPalindrome(s))
s = "hello"
print(isPalindrome(s))