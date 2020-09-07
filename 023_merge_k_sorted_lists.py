'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists):
        '''
        brute force
            traverse all linked lists and collect the values of the nodes into an array
            sort and iterate over this array to get the proper value of nodes
            create a new sorted linked list and extend it w the new nodes

            TC: O(N log N) where N = total number of nodes
                collecting all values O(N)
                stable sorting algorithm O(N log N)
                iterating for creating linked lists O(N)

            SC: O(N)
                sorting cost O(N)
                Creating a new linked list O(N)
        '''
        self.nodes = []
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

        '''
        Priortiy Queue and merge one by one

        TC: O(N log k) where k is the number of linked lists
            comparison cost reduce to O(log k) for every pop and insertion to priority queue but finding the node w the smallest value costs O(1)
            there are N nodes in the final linked list
        SC: O(N)
            O(N) creating a new linked list
            O(k)
        '''
        from queue import PriorityQueue
        # class Solution():
            # python3 uses "queue import PriorityQueue instead of from Queue"
            # ListNode definition does not include __lt__ method. to avoid this, we use a wrapper class with __lt__ method for ListNode
           class Wrapper():
                def __init__(self, node):
                    self.node = node

                def __lt__(self, other):
                    return self.node.val < other.node.val

            head = point = ListNode(0)
            q = PriorityQueue()
            for l in lists:
                if l:
                    q.put(Wrapper(l))
            while not q.empty():
                node = q.get().node
                point.next = node
                point = point.next
                node = node.next
                if node:
                    q.put(Wrapper(node))
            return head.next

        # alternative
        # providing __eq__ and __lt__ method implementation to the ListNode class
        def mergeKLists_heapq(self, lists):
            ListNode.__eq__ = lambda self, other: self.val == other.val
            ListNode.__lt__ = lambda self, other: self.val < other.val
            h = []
            head = tail = ListNode(0)
            for i in lists:
                if i:
                    heapq.heappush(h, (i.val, i))
            while h:
                node = heapq.heappop(h)[1]
                tail.next = node
                tail = tail.next
                if node.next:
                    heapq.heappush(h, (node.next.val, node.next))
            return head.next

        # alternative
        from heapq import heappop, heappush
        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            values, head, pointer = [], None, None
            for l in lists:
                while l:
                    heappush(values, l.val)
                    l = l.next
            while values:
                if head == None:
                    head = ListNode(heappop(values))
                    pointer = head
                else:
                    pointer.next = ListNode(heappop(values))
                    pointer = pointer.next
            return head

        # alternative 2
        '''
        add nodes into min heap
        pop the node from the min heap, add it to the pointer and then increment the pointer and the node
        rinse repeat until no more elements in min heap
        return head.next
        '''
        from heapq import heappop, heappush
        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            head = point = ListNode(0)
            q = []
            for l in lists:
                if l:
                    heappush(q, (l.val, id(l), l))
                    # heappush(heap, item)
            while q:
                val, nodeId, node = heappop(q)
                # heappop(heap)
                point.next = node # use node directly instead of creating a new node
                point = point.next
                node = node.next
                if node:
                    heappush(q, (node.val, id(node), node))
            return head.next

if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists((1 -> 2 -> 4), (1 -> 3 -> 4)))
