from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        longest_result = 1
        for i in nums_set:
            if i - 1 not in nums_set:
                result = 1
                current = i
                while current + 1 in nums_set:
                    result += 1
                    current += 1
                    longest_result = max(longest_result, result)
        return longest_result


if __name__ == "__main__":
    tests = []
    print(Solution().longestConsecutive(tests))
