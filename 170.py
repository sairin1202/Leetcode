class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_dic = {}
        self.numbers = []
        self.index = 0


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.num_dic[number] = self.index
        self.numbers.append(number)
        self.index += 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in range(len(self.numbers)):
            if (value - self.numbers[i]) in self.num_dic and i != self.num_dic[value - self.numbers[i]]:
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
