class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        c = 1
        j = 1
        res = ""
        while j != len(chars):
            if chars[i] == chars[j]:
                c = c + 1
            else:
                if c == 1:
                    res = res + chars[i]
                else:
                    res = res + chars[i] + str(c)
                c = 1
            j = j + 1
            i = i + 1
        if c == 1:
            res = res + chars[i]
        else:
            res = res + chars[i] + str(c)

        ls = [x for x in res]
        v = len(ls)
        print(ls)
        for i in range(len(ls)):
            chars[i] = ls[i]
        return v
