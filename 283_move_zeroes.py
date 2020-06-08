'''
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums):
        '''
        2 pointer
        loop through the array to find which number isnt a 0
        if it isnt a 0, swap the ~x index with it and increment x pointer
        '''
        x = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                x += 1
        return nums


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))
