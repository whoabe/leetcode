'''
191. Number of 1 Bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?

def hammingWeight(self, n: int) -> int:
'''


class Solution:

    def hammingWeight(self, n):
        '''
        approach 1:
            go through 32 bits
            n>>i right shift by i places
            &1 returns 1 if last bit of n>>i ==1, else 0
        '''
        res = 0
        for i in range(32):
            res += (n >> i & 1)
        return res

        '''
        approach 2:
            instead of checking every bit, repeatedly flip least significant 1 bit of the number to 0 and add 1 to the sum
            bitwise AND of n and n-1 flips the last significant bit to 0
        '''
        counter = 0
        while n:
            n = n & (n-1)
            # takes out the right most 1 of n
            counter += 1
            # update counter
        return counter


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.hammingWeight(00000000000000000000000000001011))
