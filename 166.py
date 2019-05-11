class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n = numerator
        d = denominator
        if d == 0:
            return "NaN"
        if n*d >= 0:
            flag = True
        else:
            flag = False
        n = n if n > 0 else -1*n
        d = d if d > 0 else -1*d
        first = True
        appear = {}
        res = ""
        while n % d != 0:
            # print(n , d)
            if (n, d) in appear:
                res = res[:appear[(n, d)]] + "(" + res[appear[(n, d)]:] + ")"
                return res if flag else "-"+res
            if not first:
                appear[(n, d)] = len(res)
            res += str(n // d)
            n %= d
            if n < d and first:
                res += "."
                first = False
            if n >= d:
                n //= d
            else:
                n *= 10

        res += str(n // d)
        return res if flag else "-"+res
