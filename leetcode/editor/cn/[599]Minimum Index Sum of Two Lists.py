# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
#
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。 
#
# 示例 1: 
#
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 
#
# 示例 2: 
#
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
# 
#
# 提示: 
#
# 
# 两个列表的长度范围都在 [1, 1000]内。 
# 两个列表中的字符串的长度将在[1，30]的范围内。 
# 下标从0开始，到列表的长度减1。 
# 两个列表都没有重复的元素。 
# 
# Related Topics 哈希表

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #### 先查共同点，再找所有的索引最小
        # co_list = []
        # inds = []
        # result =[]
        # for i, str1 in enumerate(list1):
        #     if str1 in list2:
        #         ind = int(i) + int(list2.index(str1))
        #         inds.append(ind)
        #         co_list.append(str1)
        # for i,ind in enumerate(inds):
        #     if ind == min(inds):
        #         result.append(co_list[i])
        #
        # return result

        ### 先构建字典（哈希），再查询
        co_list = []
        inds = []
        result =[]
        dic2 = {}
        # for i,n in enumerate(list2):
        #     dic2[n] =i
        dic2 = {n:i for i,n in enumerate(list2)}
        for i, str1 in enumerate(list1):
            j = dic2.get(str1)
            if j is not None:
                inds.append(i+j)
                co_list.append(str1)
        if len(inds) == 1:
            return co_list
        for i,ind in enumerate(inds):
            if ind == min(inds):
                result.append(co_list[i])
        return result

        ###  非常python的代码

        # d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        # return [x for x in d if d[x] == min(d.values())]


# leetcode submit region end(Prohibit modification and deletion)

###　　自建本地测试
if __name__ == '__main__':
    nums = Solution.findRestaurant(Solution, ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                   ["KFC", "Burger King", "Tapioca Express", "Shogun"]
                                   )
    print(nums)
