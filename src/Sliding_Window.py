"""
Sliding Window Module

This module provides implementations of the sliding window technique,
a common algorithm pattern for solving problems involving arrays/strings.
"""

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set() #declaring an empty setv since set doesn't allow repetition of characters
        #sliding window uses 2 pointer approach so (left and right)

    left = 0 # starting witth left=0
    result = 0 #initially result is 0, we upgrade as we go

    for right in range(len(s)): # Traverse right pointer through the string s
            
        while s[right] in charSet: #We're checking if the value already exists in the set
            charSet.remove(s[left])  #We remove the leftmost value from the set since it already exists
            left += 1 #We increment left pointer by 1
            
            # Come out of the while loop
        charSet.add(s[right]) # Add to the set if the character doesn't exist already
        result = max(result, right - left + 1) # We want to find the length of set so we find the max by subtracting right pointer (since it's greater obviously) with left pointer and add by 1 to get the actual length
        
    return result

if __name__ == "__main__":
    s = input("Enter string s:")
    print(lengthOfLongestSubstring(s))# Give me the substring of s starting at index left and ending at index right (inclusive because + 1)