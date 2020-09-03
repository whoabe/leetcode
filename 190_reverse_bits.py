'''
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Follow up:

If this function is called many times, how would you optimize it?

 

Constraints:

The input must be a binary string of length = 32

def reverseBits(self, n: int) -> int:
'''


class Solution:
    def reverseBits(self, n):
        '''
        approach:
            loop through all 32 bits
            res<<1 left shifts res by 1
            add n&1 to res to get the least significant bit
            n>>=1 right shifts n by 1 to get the next least sig bit
        '''
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.reverseBits(291671469))
