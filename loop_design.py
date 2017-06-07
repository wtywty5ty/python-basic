# range()
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

# enumerate
S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print index
    print char

# zip
ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print(zipped)

# decompose
na, nb = zip(*zipped)
print(na, nb)