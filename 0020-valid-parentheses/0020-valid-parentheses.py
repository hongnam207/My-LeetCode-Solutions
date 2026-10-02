class Solution:
    def isValid(self, s: str) -> bool:
        v = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                v.append(c)
            else:
                if c == ')':
                    if len(v) == 0:
                        return False
                    if v[-1] == '(':
                        v.pop()
                    else:
                        return False
                
                if c == ']':
                    if len(v) == 0:
                        return False
                    if v[-1] == '[':
                        v.pop()
                    else:
                        return False
                
                if c == '}':
                    if len(v) == 0:
                        return False
                    if v[-1] == '{':
                        v.pop()
                    else:
                        return False
        if len(v) == 0:
            return True
        else:
            return False