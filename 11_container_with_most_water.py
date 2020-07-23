'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

def maxArea(self, height: List[int]) -> int:
'''


class Solution(object):
    '''
    approach:
        2 pointer
            the amount of water has width that changes as the pointers do
            use max function to get the amount of water
    '''

    def maxArea(self, height):
        left, right, water = 0, len(height)-1, 0
        while right > left:
            width = right-left
            if height[left] < height[right]:
                water = max(water, height[left]*width)
                left += 1
            else:
                water = max(water, height[right] * width)
                right -= 1
        return water


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
