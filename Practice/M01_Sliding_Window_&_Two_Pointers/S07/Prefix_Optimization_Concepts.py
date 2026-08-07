from typing import List
import re

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        running_sum = 0

        for num in nums:
            running_sum += num
            answer.append(running_sum)

        return answer


def parse_numbers(raw: str) -> List[int]:
    return [int(token) for token in re.findall(r"[-+]?\d+", raw)]


if __name__ == "__main__":
    user_input = input("Enter numbers: ")
    nums = parse_numbers(user_input)
    result = Solution().runningSum(nums)
    print(result)