'''
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
'''


class Solution:
    def rotate(self, nums, k):
      # '''
      # approach 1
      #   draw out the arrays and the shifted arrays and realize that items shift by their index + the k value % the length of their numbers
      #   the easiest solution is to use a O(n-k) space solution that holds temp values
      # '''
      # n = len(nums)
      # k %= n
      # for i in range(k):
      #   temp = nums.pop()
      #   nums.insert(0, temp)
      # return nums
        '''
        approach
            k%n provides the value that the array has shifted, cant use just k because k can be greater than n
            1st reverse does the whole array
            2nd reverse does 0->k-1
            3rd reverse does k->end
        '''
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
