#LC 1248: Sliding Window variant of prefix sum
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2 Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

def SWVariantSubarraySumEqualsK(nums = list[int], k = int) -> int:
    left = 0
    result = 0
    odd_count = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            odd_count += 1
        while odd_count > k:
            if nums[left] % 2 == 1:
                odd_count -= 1
            left += 1
        result += (right - left + 1)
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the nums array:").split()))
    k = int(input("Enter the value of k:"))
    print(SWVariantSubarraySumEqualsK(nums, k))
        
