#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
#
# 示例: 
#
# 输入: [0,1,0,3,12]
#输出: [1,3,12,0,0] 
#
# 说明: 
#
# 
# 必须在原数组上操作，不能拷贝额外的数组。 
# 尽量减少操作次数。 
# 
# Related Topics 数组 双指针

from typing import List

#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### 双指针，快指针指向部位0的元素的位置，然后交换快慢指针的值。 i 遍历数组， j按顺序保存非零，
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j+=1
        # return nums

        ### 解法一：暴力搜，当碰到0，开始在当前位置之后的元素里搜索不为0的数，找到后交换数值，继续向后遍历。
        # 解答成功:
        # 执行耗时: 48ms, 击败了98.59 % 的Python3用户
        # 内存消耗: 13.8MB, 击败了99.25 % 的Python3用户
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j +=1
        for i in range(j,len(nums)):
            nums[i] = 0



#leetcode submit region end(Prohibit modification and deletion)

###　　自建本地测试函数
# if __name__ == '__main__':
#     nums = Solution.moveZeroes(Solution,[1,2,0,0,4])
#     print(nums)