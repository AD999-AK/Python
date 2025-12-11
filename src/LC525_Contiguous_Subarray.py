#LC 525: Max number of cintiguous subarra with an equal number of 0s and 1s
from typing import List
def maxBinarySubarray(nums: List[int]) -> int:
    count = {0:-1} #This means that we have seen a prefix sum of 0 before we traverse the array ensuring that we get the actual length og the array
    result = 0
    prefix = 0

    for i, num in enumerate(nums): #Here we use enumerate because we need both key and value index

        #Here we use the logic of converting all 0s to -1 and 1s to +1, this ensures that prefix[i] == prefix[j]
        # Meaning prefix[i] = (#1s up to i) - (#0s up to i) and prefix[j] = (#1s up to j) - (#0s up to j)
        # If prefix[j] == prefix [i]
        # prefix[j] - prefix[i] = 0
        if num == 0:
            prefix += -1
        else:
            prefix += 1
        if prefix in count:
            result = max(result, i - count[prefix]) #We want to maximize the result with the count of the prefix
        else:
            count[prefix] = i
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the nums array: ").split()))
    print(maxBinarySubarray(nums))