'''
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1, 2, 3]
Output: [1, 2, 4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4, 3, 2, 1]
Output: [4, 3, 2, 2]
Explanation: The array represents the integer 4

'''


class Solution(object):

    def plusOne(self, digits):
        # 1. converting the array into a string, then an integer, adding 1, converting back to string and then array
        # res = []
        # str_digits = "".join(str(i) for i in digits)
        # int_digits = int(str_digits)+1
        # str_digits = str(int_digits)
        # for i in str_digits:
        #     res.append(int(i))
        # return res
        '''
            2. add and carry
                loop through the digits starting from 1s place
                if it's less than 9, add 1 and return the number
                if not, add 0 and continue
                if the number is 9 or 99, etc then return [1] + [0] * len(digits)
        '''
        # TC: O(N), SC: O(1) when digits contains at least 1 not-9 digit else O(N)
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * len(digits)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.plusOne([1, 2, 9]))
