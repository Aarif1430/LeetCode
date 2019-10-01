from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


if __name__ == '__main__':
    twoSum = Solution()
    print(twoSum.two_sum([3, 2, 4], 6))