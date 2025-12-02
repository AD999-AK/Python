#LC974 - Subarray Sums Divisible by K

def subarraySum(nums: List[int], k: int) -> int:
    prefix = 0
    count = {0:1} #Here we count the sum and not the length(index), hence 1
    result = 0

    for num in nums:
        prefix += num #We update the prefix
        mod = prefix % k

        #To handle negative mod values
        if mod < 0:
            mod += k

        #If we have seen the sum before, we update it's count
        if mod in count:
            result += count[mod]
        
        #Otherwise we add it to the hashmap
        count[mod] = count.get(mod, 0) + 1
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers separated by space:").split()))
    k = int(input("Enter the value of k:"))
    print(subarraySum(nums, k))
