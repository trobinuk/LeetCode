class Solution:
    def romanToInt(self, s: str) -> int:
        # Input is String
        # Output is integer
        # First thoughts: dict to assign values for Symbol and respective values, for loop, check for "I, X, C" , Consider the next char check, read from dict and return
        # Issue with for loop is I want to skip reading some characters in special case like "I, X, C"  with combination
        # Time Limit exceeded for the below code. Why? I still think it's O(N). So, FUNNY THING is I ended up with a non-ending loop . Forgot to add idx+1
        # There is a change in approach, lookup for 2 chars and check in lookup (I didn't know that slicing would not give "index out of range error" it's safe), matches add up, idx +2, continue to skip it, if not skipping it will check for one and add idx +1, rdeturn result
        # I'd say the first one is logical thinking, the 2nd one with right approach is algorothmic thinking
        # Things I learned: while slicing I don't need to worry about len of index, end the loop bruh, 
        '''lookup = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        result,idx = 0,0
        strLen = len(s)-1
        while idx <= strLen:
            if idx != strLen:
                if s[idx] == "I" and s[idx+1] in ("V","X"):
                    result += lookup[s[idx:idx+2]]
                    idx += 2
                elif s[idx] == "X" and s[idx+1] in ("L","C"):
                    result += lookup[s[idx:idx+2]]
                    idx += 2
                elif s[idx] == "C" and s[idx+1] in ("D","M"):
                    result += lookup[s[idx:idx+2]]
                    idx += 2 
                else:
                    result += lookup[s[idx]]
                    idx += 1
            else:
                result += lookup[s[idx]]
                idx += 1
        return result
        '''
        lookup = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        result,idx = 0,0
        while idx < len(s):
            if s[idx:idx+2] in lookup:
                result += lookup[s[idx:idx+2]]
                idx += 2
                continue
            result += lookup[s[idx]]
            idx += 1
        return result


        








