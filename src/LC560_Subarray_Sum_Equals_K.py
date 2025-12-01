def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum = 0
    count = {0:1}
    result = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in count:
            result += count[prefix_sum - k]
        count[prefix_sum] = count.get(prefix_sum, 0) + 1
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter array separated by space:").split()))
    k = int(input("Enter k:"))
    print(subarraySum(nums, k))
