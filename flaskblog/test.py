# test = [1,0,-1]
#
# hey = list(set(test))
# hey.sort()
#
# print(hey)

class Solution:
    def longestConsecutive(self, nums):
        self.nums2 = list(set(nums))
        self.nums =self.nums2
        self.nums.sort()
        self.maxval = 0
        self.count = 1

        for i in range(len(self.nums)):
            self.dfs(i)

            if self.maxval < self.count:
                self.maxval = self.count
            else:
                self.count = 1
        return self.maxval

    def dfs(self, curr):

        if curr + 1 > len(self.nums) - 1 or self.nums[curr] == self.nums[curr+1]:
            return

        if self.nums[curr + 1] != self.nums[curr]+1:
            return

        self.count += 1
        self.dfs(curr + 1)

newobj = Solution()

print(newobj.longestConsecutive([1,0,-1]))