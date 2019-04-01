class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        # print(path)
        stack = []
        for folder in path:
            if folder == "":
                continue
            if folder == "..":
                if len(stack) > 0:
                    stack.pop()
            elif folder != ".":
                stack.append(folder)
        if len(stack) == 0:
            return "/"
        stack.insert(0,"")
        return "/".join(stack)
