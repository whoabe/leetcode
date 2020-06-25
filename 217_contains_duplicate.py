'''
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


class Solution(object):
    def containsDuplicate(self, nums):
        '''
        approach
            hash table
                make a dictionary and check if numbers are in dictionary
            sorting
                sort the items and compare the next numbers
            set
                compare the len of the original and the len of the set

        '''
        # hash table
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = i
                # doesnt matter what the value is
        return False

        # # sorting
        # if len(nums) < 2:
        #     return False
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # # set
        # return len(set(nums)) != len(nums)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 4]))
