'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        '''
        approach:
            loop through the minString and check it with the maxString
            return the minString to where it matched w the maxString
            works because the min and max evaluate the values of the ascii characters
        '''
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        minString = min(strs)
        maxString = max(strs)

        for i, c in enumerate(minString):
            if c != maxString[i]:
                return minString[:i]
                # return everything from beginning to i-1
        return minString


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
