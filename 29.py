class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # sign = 1
        # if dividend < 0 and divisor > 0 :
        #     sign = -1
        # if dividend > 0 and divisor < 0 :
        #     sign = -1
        # dividend = -1*dividend if dividend < 0 else dividend
        # divisor = -1*divisor if divisor < 0 else divisor
        # res = 0
        # while dividend - divisor >= 0:
        #     dividend -= divisor
        #     res += 1
        # return res*sign

        # binary search
        sign = 1
        if dividend < 0 and divisor > 0 :
            sign = -1
        if dividend > 0 and divisor < 0 :
            sign = -1
        dividend = -1*dividend if dividend < 0 else dividend
        divisor = -1*divisor if divisor < 0 else divisor
        res = 0
        while dividend >= divisor:
            cur_divisor = divisor
            if dividend < cur_divisor:
                return res * sign
            res_ = 1
            while cur_divisor <= dividend:
                cur_divisor = cur_divisor << 1
                res_ *= 2
            res += res_ // 2
            dividend -= cur_divisor >> 1
        if res*sign < 2**31:
            return res * sign
        else:
            return 2**31 - 1
        if res*sign > -2**31:
            return res * sign
        else:
            return -2**31
