#LC:930 Binary Subarrays Sum

def subarraySum(nums: list[int], goal: int) -> int:
    prefix = 0
    count = {0:1}
    result = 0
    # nums = [1, 0, 1, 1, 0, 1] ,goal = 2
    for num in nums:
        prefix += num
        if prefix - goal in count:
            result += count[prefix - goal]
        count [prefix] = count.get(prefix, 0) + 1
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the bianry array: ").split()))
    goal = int(input("Enter the goal: "))
    print(subarraySum(nums, goal))