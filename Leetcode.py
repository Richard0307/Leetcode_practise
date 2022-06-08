from itertools import count
from turtle import right


class Solution:
    # Leetcode_q1
    # 使用dict字典
    # 时间复杂度：O（n），空间复杂度O(n) 
    def twoSum(self, nums:List[int], target:int) -> List[int]:
            dic = {}
            for i, num in enumerate(nums):
                if num in dic:
                    return[dic[num],i]
                else:
                    dic[target-num] = i

    # Leetcode_q2
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        add = l1.val + l2.val
        res = ListNode(add % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)
        if add >= 10:
            res.next = self.addTwoNumbers(res.next, ListNode(1))
        return res
    
    # Leetcode_q3
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0    # 左边界，如有重复依次剔除最左边元素
        cur_len = 0     # 记录当前window的长度即字母个数
        max_len = 0     # 保存最长长度
        window = set() # 滑动窗口意义是遇见重复字母则以重复字母开始新建一个窗口
        for i in range (n):
            cur_len += 1
            while s[i] in window:   # 遇见重复字母则删除重复字母前的所有字母，如abcc，到第二个c时删除abc，剩余c.
                window.remove(s[left])
                left +=1
                cur_len -=1
            if cur_len > max_len: max_len = cur_len
            window.add(s[i])
        return max_len