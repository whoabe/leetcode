'''
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s, t):
        # dictionary1
        sdict, tdict = {}, {}
        for i in s:
            sdict[i] = sdict.get(i, 0) + 1
        for i in t:
            tdict[i] = tdict.get(i, 0) + 1
        return sdict == tdict

        # dictionary2
        # if len(s) == len(t):
        #     chars = defaultdict(int)
        #     for i in s:
        #         chars[i] += 1
        #     for i in t:
        #         chars[i] -= 1
        #     return all(j == 0 for j in chars.values())
        # return False

        # return collections.counter(s) == collections.counter(t)

        # return sorted(s) == sorted(t)

        # return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
