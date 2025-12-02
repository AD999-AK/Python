# Maximum size subarray sum equals K
# Prefix sum + hashmap storing first occurence index
# Input: nums = 1 -1 5 -2 3; k = 3
# Output: 4 (-1 5 -2 1) 

def maxSubarray(nums: list[int], k: int) -> int:
    prefix = 0
    count = {0: -1} #We have seen the prefix sum 0 so we initialize it's index to -1, cause we don't know where
    result = 0

    # Now we traverse through the nums array and use enumerate because it gives both value and its index
    for j, num in enumerate(nums):
        #We now update the prefix
        prefix += num

        #If we have seen the prefix sum before
        if (prefix - k) in count:
            #We update the ith index 
            i = count[prefix - k]
            result = max(result, j-i) #We want the max length so j-i will give us the length of the max subarray
        
        #If we have not seen the prefix sum before then we add it to the hashmap
        if prefix not in count:
            count[prefix] = j

    return result

if __name__=="__main__":
    nums = list(map(int, input("Enter the numbers separated by space:").split()))
    k = int(input("Enter the value of k:"))
    print(maxSubarray(nums, k))


