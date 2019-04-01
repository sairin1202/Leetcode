class Solution(object):
    def binSearch_1(self, array, target):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = (left+right)//2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left

    def binSearch_2(self, array, target):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = (left+right)//2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return False


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        rear_array = [matrix[i][-1] for i in range(len(matrix))]
        idx = self.binSearch_1(rear_array, target)
        if idx >= len(matrix):
            return False
        return self.binSearch_2(matrix[idx], target)
        
