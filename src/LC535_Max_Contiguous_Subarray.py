#LC525: Find the max subarray length where no. of 0's equals no. of 1's
#Example: Input: [0,1,0]
#Output: 2 ([0;1], [1,0])

def maxContiguousSubarray(nums: List[int]) -> int:
    prefix = 0
    count = {0:-1} #we start with -1 because we need the length and not the sum
    result = 0

    for i, num in enumerate(nums): #we use enumerate to get the index and value both to calculate length
        #we use the concept of converting 0s -> -1 and 1s -> +1
        if num == 0:
            prefix -= 1
        else:
            prefix += 1
        
        #If we have already seen the prefix before we update the result
        if prefix in count:
            result = max(result, i - count[prefix]) #i-j to calculate lenght of the subarray
        #Else we add the count to the hashmap
        else: 
            count[prefix] = i
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the series of 0s and 1s separated by space:").split()))
    print(maxContiguousSubarray(nums))
