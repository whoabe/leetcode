'''
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
'''

'''
approach:
    brute force
        check every possible prefix of that string in dictionarym if found, call for remaining portion
        TC: O(n^n), SC: O(n)
    dynamic programming
        TC: O(n^2), SC: O(n)
        divide the problem into multiple subproblems of string s1 and s2
        if substrings are in the dict, then mark that position as true 
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dic = set(wordDict)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] == True and s[i:j] in dic:
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.wordBreak("applepenapple", {"apple", "pen"}))
