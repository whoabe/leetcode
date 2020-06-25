'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


class Solution(object):
    def singleNumber(self, nums):
        '''
        approach
            list operation TC: O(N^2), SC: O(N)
                iterate over all elements
                if an element is new, append it
                if it's in the array, remove it

            dictionary TC: O(N), SC: O(N)
                iterate through all elements and set up key/value pair
                return the element that only appeared once

            math TC: O(N), SC: O(N) for set
                2*(a+b+c) - (a+a+b+b+c) = c

            bit manipulation TC: O(N), SC: O(1)
                XOR of 0 and a bit returns the bit
                XOR of two same bits returns 0
                XOR all the bits together returns the unique number

        '''
        # list operation
        no_duplicate = []
        for i in nums:
            if i not in no_duplicate:
                no_duplicate.append(i)
            else:
                no_duplicate.remove(i)
        return no_duplicate.pop()

        # dictionary
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0)+1
        for i in dict:
            if dict[i] == 1:
                return i

        # dictionary 2
        from collections import defaultdict
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1
        for i in dict:
            if dict[i] == 1:
                return i

        # math
        return 2*sum(set(nums)) - sum(nums)

        # bit maniupulation
        a = 0
        for i in nums:
            a ^= i
        return a


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.singleNumber([1, 2, 3, 4]))
