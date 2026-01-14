class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lookup = {}
        for char in s:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1
        print(lookup)
        # Scenarios where the string is palindrome
        # All Chars are even, 1 odd + remaining all even, a-3, b-3, c-2, d-2
        flag = 0
        for char,cnt in lookup.items():
            if cnt%2 == 0:
                continue
            if flag == 0:
                flag = 1
                continue
            return False  
        return True