class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        records = []
        count = 0
        record = []
        for word in words:
            count += len(word)
            if count <= maxWidth:
                record.append(word)
                count += 1
            else:
                records.append(record)
                count = len(word)
                record = [word]
                count += 1
        records.append(record)
        # print(records)
        output = []
        for j, record in enumerate(records):
            if j == len(records)-1:
                res = ""
                for i, word in enumerate(record):
                    if i == len(record)-1:
                        res += word
                        while len(res) < maxWidth:
                            res += " "
                    else:
                        res += word
                        res += " "
                output.append(res)

            else:
                count = 0
                for word in record:
                    count += len(word)
                space_num = 0
                if len(record) > 1:
                    space_num = (maxWidth - count) // (len(record)-1)
                    space_num_add = (maxWidth - count) % (len(record)-1)
                res = ""
                for i in range(len(record)):
                    res += record[i]
                    if i < len(record)-1:
                        res += " "*space_num if i>=space_num_add else " "*(space_num+1)
                    else:
                        while len(res) < maxWidth:
                            res += " "
                output.append(res)
        return output
