'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

def climbStairs(self, n: int) -> int:

'''


class Solution:
    def climbStairs(self, n):
        '''
        basically fibonacci, can use DP to solve
        https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down).
        '''
        # initializing the steps
        steps = [1, 1]
        for i in range(2, n+1):
            # since we can either take 1 or 2 steps, we add the previous step count w the i-2 step count to get the current step count
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(3))
