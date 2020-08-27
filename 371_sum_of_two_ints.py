'''
371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

def getSum(self, a: int, b: int) -> int:
'''


class Solution:
    '''
    approach:
        use bitwise operations
        1. find carry using & and << (left shift)
        2. hold addition in the a
        3. hold the carry in b

        python has no 32 bits limit need to set a mask to handle negative integers overflow
        https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks

    '''

    def getSum(self, a, b):
        carry = 0
        # 32 bit mask in hex
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > mask else a


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.getSum(1, 2))
