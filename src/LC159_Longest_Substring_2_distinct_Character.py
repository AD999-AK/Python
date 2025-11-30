# LC159: Sliding Window Pattern: Longest substring with at most 2 distinct characters

def longestSubstring(s: str) -> int:
    left = 0
    result = 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        result = max(result, right - left + 1)
    return result

if __name__ == "__main__":
    s = input("Enter string s:")
    print(longestSubstring(s))

