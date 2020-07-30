'''
322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

'''
approach:
    greedy
        doesnt work in cases like coins = 1, 15, 25 and amount is 30    
    dynamic programming
        1. top down DFS
        2. Bottom Up
    BFS Queue Recursion
'''


class Solution(object):
    def coinChange(self, coins, amount):
        #topdown (DFS)
        # if not coins:
        #     return
        # mem = {}

        # def dp(amount, coins_used=0):
        #     if amount in mem:
        #         return mem[amount]
        #     # base case
        #     if amount == 0:
        #         return 0
        #     tmp = []
        #     for coin in coins:
        #         if amount-coin >= 0:
        #             tmp.append(dp(amount-coin, coins_used+1))
        #         else:
        #             tmp.append(float('inf'))
        #     _min = min(tmp)+1
        #     mem[amount] = _min
        #     return _min
        # output = dp(amount)
        # return output if output != float('inf') else -1

        # BFS Queue recursion
        # from collections import deque
        # visited = set()
        # queue = deque([(amount, 0)])  # (remainder, coin_count)
        # coins.sort(reverse=True)
        # while queue:
        #     remainder, coin_count = queue.popleft()
        #     if remainder not in visited:
        #         if remainder == 0:
        #             return coin_count
        #         if remainder < 0:
        #             continue
        #     for coin in coins:
        #         queue.append((remainder-coin, coin_count+1))
        #     visited.add(remainder)
        # return -1

        # bottom up
        # dp = [float('inf')]*(amount+1)
        # dp[0] = 0
        # for coin in coins:
        #     for x in range(coin, amount+1):
        #         dp[x] = min(dp[x], dp[x-coin]+1)
        # return dp[amount] if dp[amount] != float('inf') else -1

        dp = []
        dp.append(0)
        for i in range(1, amount+1):
            dp.append(amount+1)
            for coin in coins:
                if coin <= i and dp[i-coin] + 1 < dp[i]:
                    dp[i] = dp[i-coin] + 1
        return dp[-1] if (dp[-1] != amount+1) else -1

        # dp = [0]*(amount+1)
        # for i in range(1, amount+1):
        #     if i in coins:
        #         dp[i] = 1
        #         continue
        #     min_coins = float('inf')
        #     for coin in coins:
        #         if i-coin >= 0:
        #             min_coins = min(dp[i-coin], min_coins)
        #     dp[i] = min_coins+1
        # if dp[-1] == float("inf"):
        #     return -1
        # return dp[-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
