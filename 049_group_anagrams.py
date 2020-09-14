'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
'''

import collections


class Solution(object):
    def groupAnagrams(self, strs):
        '''
        TC: O(N) traverse the string one character at a time and push pop operations are O(1)
        SC: O(N) worst case push all brackets onto stack

        approach:
            dictionary with the keys as the sorted words, and the values as the words
            return a list of the dictionary values

        '''
        # dict = {}
        # for i in strs:
        #     sorted_str = "".join(sorted(i))
        #     if sorted_str not in dict:
        #         dict[sorted_str] = [i]
        #     else:
        #         dict[sorted_str].append(i)
        # return list(dict.values())

        '''
        approach 2:
            dictionary with key being sorted tuple of the word and the values as the words
        TC: O(NKlogK) N is length of strs and K is the max lenght of a string in strs
            outer loop has complexity O(N)
            sorting each string takes O(KlogK) time
        SC: O(NK), total information content stored in ans
        '''
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
