def Print_Box(n):
    k = n
    Print_F_L(k)
    mid = n-2
    while mid:
        print()
        print("*", end="")
        mid_mid = n-2
        while mid_mid:
            print(" ", end="")
            mid_mid=mid_mid-1
        print("*", end="")
        mid = mid-1
    k = n
    print()
    Print_F_L(k)






def Print_F_L(k):
    while k:
        print("*", end="")
        k = k-1


Print_Box(3)



