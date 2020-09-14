'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

def isValid(self, s: str) -> bool:
'''


class Solution(object):
    def isValid(self, s):
        '''
        TC: O(N) traverse the string one character at a time and push pop operations are O(1)
        SC: O(N) worst case push all brackets onto stack

        approach:
            dictionary to match the parentheses pairs

        '''
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            else:
                if len(stack) > 0 and mapping[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isValid("{[]}"))
