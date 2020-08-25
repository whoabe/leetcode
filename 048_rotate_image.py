'''
48. Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

'''


class Solution(object):
    '''
    approach
        1. flip flip
            reverse the rows, then transpose the matrix
        2. pythonic flip flip
            ::-1 and zip(transpose)
    '''

    def rotate(self, matrix):
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix

        # pythonic
        # matrix[::] = zip(*matrix[::-1])


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
