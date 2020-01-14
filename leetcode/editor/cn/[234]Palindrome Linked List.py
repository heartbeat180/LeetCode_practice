#请判断一个链表是否为回文链表。 
#
# 示例 1: 
#
# 输入: 1->2
#输出: false 
#
# 示例 2: 
#
# 输入: 1->2->2->1
#输出: true
# 
#
# 进阶： 
#你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# Related Topics 链表 双指针
  



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        ## 保存成数组，倒序后对比
        # if head and head.next is None:
        #     return True
        # arr = []
        # while head:
        #     _,head = arr.append(head.val),head.next
        # return  arr == arr[::-1]

        # 边界条件不用忘记了
        if not (head and head.next):
            return True
        p = ListNode(-1)
        p.next, low, fast = head, p, p
        # 快慢指针不断迭代，找到中间节点
        while fast and fast.next:
            low, fast = low.next, fast.next.next
        cur, pre = low.next, None
        low.next = None
        # 将链表一分为二之后，反转链表后半部分
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        a, b = p.next, pre
        # 将链表前半部分和 反转的后半部分对比
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return True
#leetcode submit region end(Prohibit modification and deletion)
