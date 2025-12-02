#LC76: Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
from collections import Counter, defaultdict
def minWindow(s: str, t: str) -> str:
#We're checking if either t or s is empty, or if length of given substring exceeds length of string to check from, we return blank
    if not t or not s or len(t) > len(s):
        return ""
    needed = Counter(t) # needed records the hashmap of string t {a:1, b:1, c:1}
    window = defaultdict(int) #window records hashmap of current window during traversal
        
    required_distinct = len(needed) #No. of required distinct characters should be same as distinct characters in t (so len(t))
    satisfied_distinct = 0 #We add to it when we find our required distinct characters
        
    left = 0
    best_left = 0 #Here we store the left index of the min substring (initially we store 0)
    best_len = float("inf") #Here we store the length of the min substring (initially we store infinity)

    for right, ch in enumerate (s): #enumerate gives us the character and its respective index eg: {A 0, D 1, O 2, B 3, E 4, C..}
        window[ch] += 1 #We increment key of the character ch in s and add it to window

        if ch in needed and window[ch] == needed[ch]: #We check if character is there in needed(s) and its counts match (window = needed)
            satisfied_distinct += 1 # We increment satisfied distinct character count by 1

            #We then implement another loop to start shrinking
            #Fist we check while left index <= right and the satisfied distict characters count equals the required ditinct character count
        while left <= right and satisfied_distinct == required_distinct:  
            current_len = right - left + 1 #Here we update the length of the current found substring
            #If the current found substring's length is less than the best length, we update the best length and it's left index(best_left)
            if current_len < best_len : #we now check for case when the current length is < best_length
                best_len = current_len 
                best_left = left
            #We then remove the leftmost character
            left_char = s[left]
            window[left_char] -= 1
            #If while shrinking (deleting left characters) we have reduced the key count of the required character eg:{ a:0}
            if left_char in needed and window[left_char] < needed[left_char]:
                    #Then we decrease the value of satisfied distinct characters
                satisfied_distinct -= 1
            left += 1 #We then shift the left pointer by 1 to find the new minimum substring (shrinking window)

    if best_len == float("inf"):  #If after all this the best length remains unchanged(inf) -> return blank
        return ""
        #Otherwise return the length of the new found minimum substring where best_left is the left index of the substring and est_left + best_length is the end (right index) of the substring
    return s[best_left: best_left + best_len]

if __name__ == "__main__":
    s = input("Enter the string s:")
    t = input("Enter the string t:")
    print(minWindow(s, t))
            

