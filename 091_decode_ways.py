'''
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def numDecodings(self, s: str) -> int:
'''

'''
approach:
    dynamic programming
        TC: O(N) SC: O(N)

        similar to the 1,2 staircase problem

'''


class Solution(object):
    def numDecodings(self, s):
        # s starts with "0" case
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0:2] = [1, 1]
        # base case initalization
        for i in range(2, n+1):
            # 1 step jump
            if 0 < int(s[i-1:i]):
                dp[i] += dp[i-1]
            # 2 step jump
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.numDecodings("226"))
