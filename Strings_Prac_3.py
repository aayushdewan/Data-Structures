def minimumCharactersForWords(words):
    # Write your code here.
    dit = {}  # The final dict
    s = ''
    ls = []  # The final list
    for i in range(len(words)):
        count = {}  # always a new count dict created to check the count of each char in words
        for j in range(len(words[i])):
            try:
                count[words[i][j]] += 1
            except:
                count[words[i][j]] = 1
        for k, v in count.items():
            try:
                v1 = dit[k]  # {t:1} - actual dict
                v2 = max(v1, v)  # {t:2} - count dict
                dit[k] = v2  # put max value to actual dit
            except:
                dit[k] = v  # if the char not present just add the value

    print(dit)
    for k, v in dit.items():
        s = s + k * v
    ls[:0] = s  # convert string to list
    print(ls)
    return ls

