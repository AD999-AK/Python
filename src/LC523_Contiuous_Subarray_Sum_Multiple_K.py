#LC 523: Continuous Subarray Sum
# Find the contiguous subarray whose length>=2 and the sum of the subarray numbers is a multiple of k
from typing import List
def ContiguousSubarraySumMultipleK(nums: List[int], k:int) -> bool:

    # First we handle K=0 scenario
    if k == 0:
        # Then we check for two consecutive 0s so they sum up to 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        return False
    #Then we handle k = negative scenarios

    k = abs(k)

    #Then we follow classic count array length pattern
    count = {0:-1} #we start at -1, because this is a length problem
    prefix  = 0

    for i, num in enumerate(nums):
        prefix += num #we update the prefix
        rem = prefix % k #we store the remainder in rem
        #If we have already seen reminder before in count, we check if length >= 2 and return True
        if rem in count:
            if i - count[rem] >= 2: #Because i is the index where we are at, and count[rem] basically gives us the index value of rem
                #Bcause in the hashmap we store {key:value} here {rem:index of rem}
                return True
        #If not then we store the count(index of rem) in hashmap
        count[rem] = i
    return False

if __name__ == "__main__":
    nums = list(map(int, input("Enter the values of array nums: ").split()))
    k = int(input("Enter the value of k: "))
    print(ContiguousSubarraySumMultipleK(nums, k))

