'''
67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''


class Solution:
    def addBinary(self, a, b):
        '''
        bit by bit computation
            zfill a and b to whatever the longest length a or b is
            do a for loop in reverse to add and carry the numbers
            check what the carry value yields and append it to ans
            after the loop is done, check carry value to see whether or not to add 1
        '''
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        # zfill fills string w 0s until it is n characters long
        carry = 0
        ans = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            # now we need to find the ans value of the last bit
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            # if the bits carried over, need to change carry for the next bit
            carry //= 2
        if carry == 1:
            ans.append("1")
        ans.reverse()
        return ''.join(ans)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.addBinary("1010", "1011"))
