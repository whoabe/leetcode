'''
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

def longestPalindrome(self, s: str) -> str:
'''


class Solution(object):
    '''
    approach 1:
        brute force
            create every possible substring starting from i and adding one character and check if its a palindrome
            looping through the substrings is O(N^2) and checking if its valid is O(N)
            TC: O(N^3)
    '''

    # def longestPalindrome(self, s):
    #     if len(s) == 1:
    #         return s
    #     if len(s) < 1:
    #         return ""
    #     maxSubstring = s[0]
    #     for i in range(len(s)):
    #         currentSubstring = s[i]
    #         for j in range(i + 1, len(s)):
    #             currentSubstring += s[j]
    #             if (self.isPalindrome(currentSubstring) and
    #                     len(currentSubstring) > len(maxSubstring)):
    #                 maxSubstring = currentSubstring
    #     return maxSubstring

    # def isPalindrome(self, s):
    #     left = 0
    #     right = len(s) - 1
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    '''
    approach 2:
        dynamic programming
        TC: O(N^2)
        SC: O(N^2) to store table
    '''

    # def longestPalindrome(self, s):
    #     n = len(s)
    #     # Bottom up 2D array to store the dp[i][j] if its a palindrome or not
    #     dp = [[False]*n for _ in range(n)]

    #     ans = ''

    #     # the dp for the individual characters will be True since a letter by itself is a palindrome. also set the ans to be the letter
    #     # every string w one letter is a palindrome
    #     for i in range(n):
    #         dp[i][i] = True
    #         ans = s[i]

    #     for start in reversed(range(n)):
    #         for end in range(start+1, n):
    #             # palindrome condition
    #             # check if the start and end of the substring are equal
    #             if s[start] == s[end]:
    #                 # if it's a two char. string or if the remaining string is a palindrome too
    #                 if end - start == 1 or dp[start+1][end-1]:
    #                     dp[start][end] = True
    #                     # check if the current substring is longer than the current ans
    #                     if len(ans) < end-start+1:
    #                         ans = s[start: end + 1]
    #     return ans

    '''
    approach 3:
        expand around center
        TC: O(N^2)
        SC: O(1)
    '''

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestPalindrome("babad"))
