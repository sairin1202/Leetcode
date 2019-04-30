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
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        times = n // 4
        count = 0
        for t in range(times):
            res = [0] * 4
            c = read4(res)
            count += c
            for i in range(c):
                buf[t*4+i] = res[i]
            if c < 4:
                return count

        res = [""] * 4
        read4(res)
        count = count + n % 4
        for i in range(n % 4):
            buf[times*4+i] = res[i]
        return count

        
