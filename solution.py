class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        A = matrix

        for i in range(n):
            for j in range(i+1,n):
                A[i][j],A[j][i] = A[j][i] , A[i][j]

        for i in range(n):
            for j in range(n // 2):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
