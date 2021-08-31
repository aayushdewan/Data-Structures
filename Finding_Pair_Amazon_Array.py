s = [0, -1, 2, -3, 1]
dit={}
val=0
num=-2
f=0
for i in range(len(s)):
    val=num-s[i]  # basic logic s[i]+x=num so x=num-s[i]
    try:
        if dit[val]:
            print(val)
            f=1
            break
    except:
        dit[s[i]]=1
if f==0:
    print("No pair")
else:
    print("Yes pair")






