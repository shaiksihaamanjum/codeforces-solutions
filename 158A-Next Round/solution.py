n,k=map(int,input().split())
count=0 

scores=list(map(int,input().split()))
value=scores[k-1]
for i in scores:
    if(i>=value and i>0):
        count+=1 
print(count)    
git add "158A-Next Round"
git commit -m "Add 158A-Next Round "