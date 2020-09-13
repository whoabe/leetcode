'''
424. Longest Repeating Character Replacement
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

def characterReplacement(self, s: str, k: int) -> int:
'''

from collections import Counter


class Solution(object):
    def characterReplacement(self, s, k):
        '''
        TC: O(N)
        SC: O(N)

        approach 1:
            sliding window
            window ranges from index start to len(s)
            look at chars in this window and keep track of counts
            using dict
        '''
        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            # add 1 to char count or set to 0
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result

        '''
        approach 2:
            using counter
        '''
        start = res = 0
        count = Counter()
        for end in range(len(s)):
            count[s[end]] += 1
            max_count = count.most_common(1)[0][1]
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            res = max(res, end-start+1)
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
