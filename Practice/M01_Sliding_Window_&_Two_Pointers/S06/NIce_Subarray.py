from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        current_odd_count = 0
        nice_subarrays = 0

        for num in nums:
            current_odd_count += num % 2

            target = current_odd_count - k
            if target in prefix_counts:
                nice_subarrays += prefix_counts[target]

            prefix_counts[current_odd_count] = prefix_counts.get(current_odd_count, 0) + 1

        return nice_subarrays


if __name__ == "__main__":
    solution = Solution()
    example_nums = [1, 1, 2, 1, 1]
    example_k = 2
    print(solution.numberOfSubarrays(example_nums, example_k))