l=[]
f=open('names.txt')
f=f.readlines()

for w in f:

    l.append(w.rstrip())
    
print(l)
