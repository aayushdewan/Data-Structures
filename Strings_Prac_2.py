def firstNonRepeatingCharacter(string):
    # Write your code here.
    dit = {} # creating diticionary
    st = ''
    for i in range(len(string)):
        try:
            dit[string[i]] += 1  #count the occurnece in the dit
        except:
            dit[string[i]] = 1
    for k, v in dit.items():
        if v == 1:  #if the occurance is 1 then break
            st = st + k
            break

    if st == '':
        return -1
    else:
        return string.index(st)
