'''
387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
'''


class Solution:
    def firstUniqChar(self, s):
        # dictionary1
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0)+1
        for i in dict:
            if dict[i] == 1:
                return s.index(i)
        return -1

        # dictionary2
        # count = collections.counter(s)
        # for i, letter in enumerate(s):
        #     if count[letter] == 1:
        #         return i
        # return -1

        # string slicing
        # if not s:
        #     return -1
        # if len(s) == 1:
        #     return 0
        # for i, letter in enunmerate(s):
        #     if letter not in s[:i] + s[i+1:]:
        #         return i
        # return -1


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))
