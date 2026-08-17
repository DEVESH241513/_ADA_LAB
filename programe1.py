from typing import List

class Solution:

    # Binary Search
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    # Power Function
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result = result * x

            x = x * x
            n = n // 2

        return result


# Main program
obj = Solution()

# Search
nums = [1, 3, 5, 7, 9, 11]
target = 7

print("Array:", nums)
print("Target:", target)
print("Index:", obj.search(nums, target))

# Power
x = 2.0
n = 10

print("Base:", x)
print("Exponent:", n)
print("Power:", obj.myPow(x, n))