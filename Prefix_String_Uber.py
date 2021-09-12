def Helper(a, b):
    ls = set()
    st = ''
    for i in range(len(a)):
        st = st + ''.join([str(x) for x in a[i]])
        print(st)
        ls.add(st)
    f = 0
    for j in b:
        if j not in ls:
            f = 1
            print('False')
            return

    if f == 0:
        print('True')
        return


Helper(["one", "two", "three"], ["one", "onetwo", "twothree"])

# suppose a is len n and b is len m time complexity is O(M+N) and space is O(N)


