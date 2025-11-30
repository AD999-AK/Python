# LC340: Problem Statement:
# Given a string s and an integer k,return the length of the longest substring that contains at most k distinct characters.
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: "ece" 

def longestSubstringKdistinct(s: str, k: int) -> int:
    left = 0
    count = {}
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1 # 0 is default value, +1 means we increment key count by 1 everytime there's a repitition

        while len(count) > k: #If the count exceeds K
            count[s[left]] -= 1 #We shrink the window by decreasing the key count
            if count[s[left]] == 0: #If the count becomes 0, we delete it from the dictionary
                del count[s[left]]
            left += 1 #We then increment left pointer
        result = max(result, right - left + 1) #Gives the size of the substring
    return result

if __name__ == "__main__":
    s = input("Enter String s:")
    k = int(input("Enter value of K:"))
    print (longestSubstringKdistinct(s,k))


