'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s):
        # 2 pointers
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left].isalnum():
                left += 1
            while left < right and s[right].isalnum():
                right -= 1
            if left < right and s[left].islower() != s[right].islower():
                return False
            left += 1
            right -= 1
        return True

        # check reverse
        # s = [i for i in s.lower() if i.isalnum()]
        # return s == s[::-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
