class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        len1 = len(version1)
        len2 = len(version2)
        print(version1)
        print(version2)
        for i in range(min(len1, len2)):
            if int(version1[i]) < int(version2[i]):
                return -1
            if int(version1[i]) > int(version2[i]):
                return 1
        if i+1 < len2:
            for j in range(i+1, len2):
                if int(version2[j]) != 0:
                    return -1
        if i+1 < len1:
            for j in range(i+1, len1):
                if int(version1[j]) != 0:
                    return 1
        return 0
