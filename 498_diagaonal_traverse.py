# 498. Diagonal Traverse

# Given a matrix of M x N elements(M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.


# Example:

# Input:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Output:  [1, 2, 4, 7, 5, 3, 6, 8, 9]

# Explanation:


# Note:

# The total number of elements of the given matrix will not exceed 10, 000.

class Solution(object):
    def findDiagonalOrder(self, matrix):
        # approach:
        # goes through the matrix and adds the values w the keys as i+j(row+column)
        # adds values from the dictionary
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        mp = {}
        for i in range(M):
            for j in range(N):
                if i+j in mp:
                    mp[i+j].append(matrix[i][j])
                else:
                    mp[i+j] = [matrix[i][j]]

        rs = []
        rev = True
        print(mp)
        for i in range(0, M+N-1):
            if rev:
                mp[i] = mp[i][::-1]
            rev = not rev
            rs.extend(mp[i])
        return rs


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
