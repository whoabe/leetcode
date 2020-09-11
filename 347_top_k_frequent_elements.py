'''
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        '''
        approach 1:
            heap
                build a hash map element to store the frequency
                use Counter
                O(N) time complexity, N is the number of elements in the list

                build heap of size k using N elements
                TC: avg O(K), and worst O(klogk)

                convert the heap into output array which is done in O(klogk) time
            TC: O(N log k) if k<N and O(N) if N = k
            SC: O(N + k) to store the hash map
        '''
        #import Counter
        if len(nums) == k:
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
        # heapq.nlargest(n, iterable[, key])
        # returns list w n largest elements defined by iterable key


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
