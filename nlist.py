import torch
words=[]
f=open('names.txt')
f=f.readlines()

for w in f:

    words.append(w.rstrip())
    
b={}
for w in words:
    lw=["<S>"]+ list(w) +["<E>"]
    for i , j in zip(lw,lw[1:]):
        pair=(i,j)
        b[pair]=b.get(pair,0)+1
        
        # print(i," ",j)
#print
p=sorted(b.items(),key=lambda kv:-kv[1])
#print(p)    #main to use

a=torch.zeros((3,5))

print(a)
a[1][3]=1
print(a)