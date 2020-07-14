'''
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        '''
        2 pointers, start from end
        '''
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                # if the m value is greater than the n value, set the last element to the m value
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                # set the last value to the n value
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # add missing elements from nums2
        nums1[:n] = nums2[:n]
        return nums1


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
