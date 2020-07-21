'''
326. Power of Three
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''


class Solution(object):
    def isPowerOfThree(self, n):
        # recursion
        if n == 3 or n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfThree(n/3)

        # iteration
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

        # integer limitations
        # 3^19 divisble by n
        return n > 0 and 1162261467 % n == 0

        # math
        from math import log
        if n < 1:
            return False
        return round(log(n, 3), 9) == round(log(n, 3))


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPowerOfThree(27))
