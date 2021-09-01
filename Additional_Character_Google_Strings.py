# your code goes here
def helper(s, t):
    if len(s) == 0 and len(t) == 0:
        return " "
    if len(s) == 0 and len(t) != 0:
        return t

    dit1 = {}
    dit2 = {}
    for i in s:
        try:
            dit1[i] += 1
        except:
            dit1[i] = 1
    for j in t:
        try:
            dit2[j] += 1
        except:
            dit2[j] = 1
    print(dit1)
    print(dit2)
    res = ""
    f = 0
    for k, v in dit2.items():
        try:
            v1 = dit1[k]
            v2 = dit2[k]
            if v1 == v2:
                continue
            else:
                res = k
                f = 1
                break
        except:
            res = k
            f = 1
            break
    if f==1:
        return res
    else:
        return " "



print(helper("aab","baab"))

