"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
"""



class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.extendPalindrome(s, i, i)
            len2 = self.extendPalindrome(s, i, i+1)
            
            length = max(len1, len2)
            
            if length > (end-start):
                start = i - (length-1)//2
                end = i + length//2
            
        return s[start: end+1]
        
    def extendPalindrome(self, s, left, right):
        L = left
        R = right
            
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L-= 1
            R+= 1
            
return R-L-1
