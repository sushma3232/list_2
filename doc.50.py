a=[[10,20],[30,40],[50,60],[30,20,80]]
b=[[61],[12,14,15],[12,13,19,20],[12]]
c=[]
i=0
while i<len(a):
    num=a[i]+b[i]
    c.append(num)
    i=i+1
print(c)


a=[["a","b"],["b","c","d"],["e","f"]]
b=[["p","q"],["p","s","t"],["u","v","w"]]
c=[]
i=0
while i<len(a):
    num=a[i]+b[i]
    c.append(num)
    i=i+1
print(c)


a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
while i<len(a):
    a[i].extend(b[i])
    i=i+1
print(a)