class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = [0]*len(ratings)
        right = [0]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] +1
        # print(left)
        # print(right)
        sum_ = 0
        for i in range(len(right)):
            sum_ += max(right[i], left[i])
        return sum_ + len(ratings)
        
