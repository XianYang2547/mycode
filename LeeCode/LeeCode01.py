'''
爱生活，爱Python
-- coding: UTF-8  --
@Time : 2021/11/1 10:30
@Author : Xianyang
@Email : xy_mts@163.com
@File : LeeCode01.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''


'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

'''
li=[3,2,4]
target=6
class Solution:
    def twoSum(self, li, target):
        for i in range(len(li)):
            for j in range(len(li)):
                if li[i]+li[j]  == target and i!=j :
                   return [i,j]
S=Solution()
index=S.twoSum(li,target)
print(index)