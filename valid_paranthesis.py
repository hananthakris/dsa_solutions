def isValid(s):
        if len(s) == 1 or len(s) == 0:
            return False
        charmap = { ")": "(", "}": "{", "]":"[" }
        stack = []
        for i in s:
            if i in charmap and stack:
                if charmap[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack
