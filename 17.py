class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dict = {'2':["a","b","c"],
                '3':["d","e","f"],
                '4':["g","h","i"],
                '5':["j","k","l"],
                '6':["m","n","o"],
                '7':["p","q","r","s"],
                '8':["t","u","v"],
                '9':["w","x","y","z"]}
        init_list = [""]
        for i, dit in enumerate(digits):
            pre_list = init_list[:]
            init_list = []
            for pre in pre_list:
                for c in dict[dit]:
                    init_list.append(pre+c)
        return init_list

        
