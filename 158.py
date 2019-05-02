"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.temp = []
        self.eof = False

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count = 0
        idx = 0
        tmp_len = len(self.temp)
        if self.eof:
            return 0
        if len(self.temp):
            if len(self.temp) >= n:
                for i in range(n):
                    buf[idx+i] = self.temp.pop(0)
                return n
            else:
                n -= len(self.temp)
                for i in range(len(self.temp)):
                    buf[idx+i] = self.temp[i]
                idx = tmp_len
                count += tmp_len
                self.temp = []
        for i in range(n//4):
            res = [""]*4
            c = read4(res)
            if c < 4:
                for j in range(c):
                    buf[j+idx] = res[j]
                self.eof = True
                return count + c
            for j in range(4):
                buf[j+idx] = res[j]
            count += c
            idx += 4
        res = [""]*4
        remain = n % 4
        c = read4(res)
        if c > remain:
            for i in range(remain):
                buf[i+idx] = res[i]
            for i in range(remain, c):
                self.temp.append(res[i])
            return count+remain
        else:
            for j in range(c):
                buf[j+idx] = res[j]
            self.eof = True
            return count + c

        
