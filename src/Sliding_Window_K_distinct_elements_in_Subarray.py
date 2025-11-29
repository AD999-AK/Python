def totalFruit(fruits: List[int]) -> int:
# Explicitly handle empty array case

    if len(fruits) == 0:
        return 0
    #Initializing pointers starting at 0, creating empty dictionary and result is 0   

    left = 0
    count = {}
    result = 0
    
    for right in range(len(fruits)): #Right pointer traveses the fruits array end to end
        count[fruits[right]] = count.get(fruits[right], 0) + 1 #We increase the count of the key and return default value 0 if it doesn't exits

        while len(count) > 2: #Since we can only have 2 distinct element, so if the key count increases > 2 we decrement left pointer by by 1
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0: #If the count becomes 0, then we delete the key from the dictionary
                del count[fruits[left]]
            left += 1 #We increment the left pointer now

        result = max(result, right - left + 1) #WE get the result (size of subarray) by subracting right - left and adding 1 to get the actual size
    return result

if __name__ == "__main__":
    raw = list(map(int, input("Enter the input fruits array: ").split()))
    print(totalFruit(raw))
    
