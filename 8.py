class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        first_word = None
        flag = 1
        s = ""

        for i in range(len(str)):
            if not (str[i] <="9" and str[i] >= "0"):
                if first_word != None:
                    break
                else:
                    if str[i] == "+":
                        flag = 1
                        first_word = "+"
                    elif str[i] == "-":
                        flag = -1
                        first_word = "-"
                    else:
                        return 0
            else:
                if first_word == None:
                    first_word = str[i]
                s += str[i]
        if len(s):
            if int(s)*flag >= 2**31-1:
                return 2**31-1
            elif int(s)*flag <=-2**31:
                return -2**31
            else:
                return int(s)*flag
        else:
            return 0
