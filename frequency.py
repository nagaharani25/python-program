s=[1,2,3,4,5,6,7,8]
res=[]
freq={}
for num in s:
    freq[num]=freq.get(num,0)+1
for val in freq:
    if freq[val]>1:
        res.append(val)
print(res)        
