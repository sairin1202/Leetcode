from collections import Counter
class Solution(object):
    def gcd(self, x, y):
        if x == 0 and y == 0:
            return 1
        if y == 0:
            return x
        return self.gcd(y, x%y)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        hash_table = {}
        counter_points = [tuple(point) for point in points]
        counter = Counter(counter_points)

        res = 1
        for i in range(1, len(points)):
            for j in range(i):
                cur_point = points[i]
                x1 = cur_point[0]
                y1 = cur_point[1]
                pre_point = points[j]
                x2 = pre_point[0]
                y2 = pre_point[1]

                if y1 - y2 == 0 and x1 - y2 != 0:
                    line = (0, y1, 0, 0)
                elif x1 - x2 == 0 and y1 - y2 != 0:
                    line = (x1, 0, 0, 0)
                else:
                    times1 = self.gcd(y1-y2, x1-x2)
                    times2 = self.gcd(y1*x2 - y2*x1, x2-x1)
                    line = ((y1-y2)//times1, (x1-x2)//times1, (y1*x2 - y2*x1)//times2, (x2-x1)//times2)
                if line in hash_table:
                    hash_table[line].add(tuple(points[i]))
                    hash_table[line].add(tuple(points[j]))
                else:
                    hash_table[line] = set()
                    hash_table[line].add(tuple(points[i]))
                    hash_table[line].add(tuple(points[j]))

        for line, points in hash_table.items():
            count = 0
            for point in points:
                count += counter[point]
            res = max(res, count)

        return res
