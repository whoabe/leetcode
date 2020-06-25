'''
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        '''
        approach
            two pointers
                recommended when the input is sorted or the output needs to be sorted
            dictionary
                collect numbers and their occurence in one array into a dictionary and then check the second array against the dictionary and check occurence


        '''
        # two pointers
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            diff = nums1[i]-nums2[j]

            if diff == 0:
                res.append(nums1[i])
                i += 1
                j += 1
            elif diff < 0:
                i += 1
            else:
                j += 1
        return res

        # dictionary
        # res = []
        # dict = {}
        # for i in nums1:
        #     dict[i] = dict.get(i, 0)+1
        # for j in nums2:
        #     if j in dict and dict[j] > 0:
        #         res.append(j)
        #         dict[j] -= 1
        # return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
