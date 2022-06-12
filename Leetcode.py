from ast import Del
from itertools import count
from turtle import right
from typing import Counter


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
    
    # Leetcode_q4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)       
        nums1.sort()
        length = len(nums1)
        if length ==1 :
            return nums1[0]
        elif length == 0:
            return 0
        elif length %2 == 0: 
            index1 = int(length/2)
            index2 = index1-1
            return(nums1[index2]+nums1[index1])/2
        elif length %2 == 1:
            index3 = int(length/2)
            return (nums1[index3])
        

    def longestPalindrome(self, s):
        size = len(s)
        if size <=1:
            return s
        # 二维 dp 问题
            # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
            # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range (size)]

        longest_l = 1
        res = s[0]

        for r in range (1,size):
            for l in range (r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                    # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                    # 否则要继续看收缩以后的区间的回文性
                    # 重点理解 or 的短路性质在这里的作用
                    if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                        dp[l][r] = True
                        cur_len = r - l + 1
                        if cur_len > longest_l:
                            longest_l = cur_len
                            res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res

    def convert(self, s: str, numRows: int) -> str:
        cache = [i for i in range (numRows)] + [i for i in range(1,numRows-1)][::-1]
        res = [""]*numRows
        for i,c in enumerate(s):
            res[cache[i%len(cache)]]+=c
        return"".join(res)

    
   

