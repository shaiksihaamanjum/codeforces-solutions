l=[]
for i in range(5):
    r=list(map(int,input().split()))
    l.append(r)

for i in range(5):
    for j in range(5):
        if(l[i][j]==1):
            r=i 
            c=j 
print(abs(r-2)+abs(c-2))
                    

           
