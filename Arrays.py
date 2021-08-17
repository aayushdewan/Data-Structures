st = "All is Well!" # expected output is Well! is All
ls = [] #convert string to ls with ls=["All"," ", "is"," ","Well!"]
start = 0 #start with 0
k = '' # to store the reversed string
for i in range(len(st)):
    if st[i] == " ": # Suppose the i has travelled will All_ so ji right now is 3
        ls.append(st[start:i]) #ls will append from [0 to i) so ls will be ls=["All"]
        start = i # start will be 3
    elif st[start] == " ": #Now at this point ls will append " "
        ls.append(" ")
        start = i # now start will be 4
ls.append(st[start:i])
print(ls)
for i in range(len(ls) - 1, -1, -1):
    k = k + ''.join(ls[i])
print(k)

