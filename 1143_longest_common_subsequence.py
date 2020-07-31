'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

def longestCommonSubsequence(self, text1, text2):
'''

'''
approach:
    brute force
        iterate through each subsequence of the first string and check if its not also a subsequence of the 2nd
        will take 2^L complexity L is the length of the string
    dynamic programming
        TC: O(m*n), SC: O(m*n) m= length of str1, n= length of str2
        the smallest subproblem is one letter left in each word
        do the azb aab example and make a table or flow chart/graph

    
'''


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        # for col in reversed(range(len(text2))):
        #     for row in reversed(range(len(text1))):
        #         if text2[col] == text1[row]:
        #             dp[row][col] = 1 + dp[row+1][col+1]
        #         else:
        #             dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        # return dp[0][0]

        # alternate dp
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for row in range(1, m+1):
            for col in range(1, n+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])
        return dp[m][n]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))
