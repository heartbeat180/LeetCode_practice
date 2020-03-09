#给定一个链表，判断链表中是否有环。 
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
#
# 
#
# 示例 1： 
#
# 输入：head = [3,2,0,-4], pos = 1
#输出：true
#解释：链表中有一个环，其尾部连接到第二个节点。
# 
#
# 
#
# 示例 2： 
#
# 输入：head = [1,2], pos = 0
#输出：true
#解释：链表中有一个环，其尾部连接到第一个节点。
# 
#
# 
#
# 示例 3： 
#
# 输入：head = [1], pos = -1
#输出：false
#解释：链表中没有环。
# 
#
# 
#
# 
#
# 进阶： 
#
# 你能用 O(1)（即，常量）内存解决此问题吗？ 
# Related Topics 链表 双指针
  



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # ## 建立哈希表，查询重复
        # s = set()
        # while head is not None:
        #     if head in s:
        #         return True
        #     _,head = s.add(head),head.next
        # return False

        ## 双指针
        if  (head and head.next) is None :
            return False
        slow = head
        fast = head.next
        while fast and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
#leetcode submit region end(Prohibit modification and deletion)
