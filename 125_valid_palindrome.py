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
        start, end = 0, len(s)-1
        while start < end:
            if not s[start].isalnum():
                start +=1
            elif not s[end].isalnum():
                end -=1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start +=1
                    end -=1
        return True

        # check reverse
        # s = [i for i in s.lower() if i.isalnum()]
        # return s == s[::-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
