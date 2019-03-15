class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = []
        # for i, c in enumerate(s):
        #     if c == "(" or c == "[" or c == "{":
        #         stack.append(c)
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         if c == ")" and stack[-1] == "(":
        #             stack.pop()
        #         elif c == ")" and stack[-1] != "(":
        #             return False
        #         elif c == "}" and stack[-1] == "{":
        #             stack.pop()
        #         elif c == "}" and stack[-1] != "{":
        #             return False
        #         elif c == "]" and stack[-1] == "[":
        #             stack.pop()
        #         elif c == "]" and stack[-1] != "[":
        #             return False
        # if len(stack):
        #     return False
        # else:
        #     return True
        id1 = 0
        id2 = 0
        id3 = 0
        for i, c in enumerate(s):
            if c == "{":
                id1 += 1
            if c == "}":
                id1 -= 1
                if id1 < 0:
                    return False
            if c == "[":
                id2 += 1
            if c == "]":
                id2 -= 1
                if id2 < 0:
                    return False
            if c == "(":
                id3 += 1
            if c == ")":
                id3 -= 1
                if id3 < 0:
                    return False
        if id1 == 0 and id2 == 0 and id3 == 0:
            return True
        else:
            return False

        
