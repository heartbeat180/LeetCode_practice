#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
#
# 示例: 
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
# 
# Related Topics 数组 哈希表

# #leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ###　　纯暴力解法，复杂度太高
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        ###  创建新list， 找减数是否在其中，并且只从num[i]的前或后面查找
        # j = -1
        # for i in range(len(nums)):
        #     temp = nums[i+1:]
        #     if (target - nums[i]) in temp :
        #         j = temp.index(target - nums[i])
        #         j += (i+1)
        #     if j>=0:
        #         return [i,j]

        ###  用字典模拟哈希查询过程
        # hashmap = {}
        # for ind, num in enumerate(nums):
        #     hashmap[num] = ind
        # for i,num in enumerate(nums):
        #     j = hashmap.get(target - num)
        #     if j is not None and i!=j:
        #         return  [i,j]

        ###  用字典模拟哈希查询过程, 并做改进，只在num[i]前面找. 速度最快
        hashmap = {}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None :
                return  [hashmap.get(target - num),i]
            hashmap[num] = i



#leetcode submit region end(Prohibit modification and deletion)

