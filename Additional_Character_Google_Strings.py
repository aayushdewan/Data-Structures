# your code goes here
s = "mman"
t = "mbmna"
t = sorted(t) #sort
s = sorted(s) #sort
f = 0
print(s)
print(t)
for i in range(len(s)):
    if s[i] != t[i]:
        f = 1
        # print(t[i])
        break
if i != len(t) - 1 and f == 0:       #this case is written in case we have the last unmatched value
    print(t[i + 1])
if f == 1:
    print(t[i])
print(" ")	

#time complexity is O(nlogn)