class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [False] * 10000
        ans = 0
        r = -1
        for l in range (0 , len(s)):
            # print(l , r)
            if r < l:
                r = l - 1
            while(r < len(s) - 1):
                r += 1
                if arr[ord(s[r])] == True:
                    r -= 1
                    break
                else:
                    arr[ord(s[r])] = True
                    # print(l , r)
                    # print(arr[:7])
                    
                    ans = max(ans , r - l + 1)
            
            # print(ans)
            
            arr[ord(s[l])] = False
        return ans