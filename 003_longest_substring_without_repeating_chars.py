'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(self, s: str) -> int:
'''


class Solution(object):
    '''
    approach:
        sliding window
    '''

    def lengthOfLongestSubstring(self, s):
        # string
        seen = ''
        mx = 0
        for c in s:
            if c not in seen:
                seen += c
            else:
                seen = seen[seen.index(c)+1:]+c
            mx = max(mx, len(seen))
        return mx

        # dictionary
        # seen = {}
        # l = 0
        # output = 0
        # for r in range(len(s)):
        #     if s[r] not in seen:
        #         output = max(output, r-l+1)
        #     else:
        #         if seen[s[r]] < l:
        #             output = max(output, r-l+1)
        #         else:
        #             l = seen[s[r]] + 1
        #     seen[s[r]] = r
        # return output


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
