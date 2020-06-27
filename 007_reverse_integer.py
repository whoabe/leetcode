'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x):
        '''
        string slicing
            convert x to a string, reverse and/or slice it and then convert back to int
        '''
        # res = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1::][::-1])

        # if -2**31 <= res <= (2**31)-1:
        #     return res
        # else:
        #     return 0

        '''
        math
        '''
        res = 0
        y = abs(x)
        while y:
            res = res*10 + y % 10
            y //= 10
        return (-res if x < 0 else res) if res.bit_length() < 32 else 0


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.reverse(-124))
