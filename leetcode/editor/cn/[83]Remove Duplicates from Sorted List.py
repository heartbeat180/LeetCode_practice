#给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
#
# 示例 1: 
#
# 输入: 1->1->2
#输出: 1->2
# 
#
# 示例 2: 
#
# 输入: 1->1->2->3->3
#输出: 1->2->3 
# Related Topics 链表
  



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ## 建立哈希表查询，哨兵节点，前指针
        s = set()
        head_head = ListNode(0)
        head_head.next = head
        pre = head_head
        while head:
            if head.val in s:
                pre.next = head.next
            else:
                pre = head
            s.add(head.val)
            head = head.next
        return head_head.next
#leetcode submit region end(Prohibit modification and deletion)
