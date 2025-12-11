#LC:560 Subarray Sum equals K
from typing import List
def SubarraySumEqualsK(nums: List[int], k: int) -> int:

    count = {0:1}
    prefix = 0
    result = 0

    for num in nums:
        prefix += num
        if prefix - k in count:
            result += count[prefix -k]
        count[prefix] = count.get(prefix, 0) + 1
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter the value of k: "))
    print(SubarraySumEqualsK(nums, k))