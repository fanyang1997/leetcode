class Solution(object):
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        hash_map = {}
        """
        enumerate-> enumerate() 函数用于将一个可遍历的数据对象
        (如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        """
        for index, value in enumerate(nums):
            hash_map[value] = index
        print(hash_map)
        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                # print(hash_map[target - value])
                if index1 != index2:
                    return [index1 + 1, index2 + 1]

# test case
numbers = {2, 7, 11, 15}
target = 9
TestCase = Solution()
print(TestCase.twoSum(numbers, target))
