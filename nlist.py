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
print(b)
