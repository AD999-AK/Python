#LC 1248: Count no of nice subarray in an array where nice meand that we have k odd numbers in the subarray

def niceSubarray(nums: List[int], k: int) -> int:
    prefix = 0
    result = 0
    count = {0:1} #Here it means that we have already seen prefix sum 0 so it enables subarrays starting at index 0

    for num in nums:
        prefix += (1 if num%2 != 0 else 0) #Here we convert odds to 1 and even to 0 so as to count exactly k odd nos
        
        #If we have seen the prefix sum before then we add it to the result
        if prefix - k in count:
            result += count[prefix - k]
        
        #Else we store it in the hashmap and increase its key count by 1
        count[prefix] = count.get(prefix, 0) + 1
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array separated by space:").split()))
    k = int(input("Enter the no. of odd nos. (k):"))
    print(niceSubarray(nums, k))