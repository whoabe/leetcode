'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

def search(self, nums: List[int], target: int) -> int:
'''


class Solution(object):
    def search(self, nums, target):
        '''
        approach
            binary search TC: log(n)
            case if target in 0->mid
                case 1: no drop 0,t,mid
                case 2: drop before target t,mid,0
                case 3: drop after target mid, 0, t
        '''
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= target < nums[mid] or target <= nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                right = mid - 1
            else:
                left = mid+1
        return -1


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
