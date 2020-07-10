'''
1089. Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9

def duplicateZeros(self, arr: List[int]) -> None:
'''


class Solution:
    def duplicateZeros(self, arr):
        # standard way TC: O(N^2) due to pop and insert having O(N) SC: O(1)
        '''
        go thru the array and check if the item is 0, if yes, then pop the array and insert 0 at the index then increment the index
        else increment the index
        '''
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 1
            i += 1
        return arr

        # backwards, couting 0s and shifting items location
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i+zeroes] = 0


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
