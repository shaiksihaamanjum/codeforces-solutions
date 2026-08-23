n=int(input().strip())
home=[]
guest=[]
answer=0
for i in range(n):
    h,a=list(map(int,input().strip().split()))
    home.append(h)
    guest.append(a)
for i in range(n):
    for j in range(n):
        if(i!=j and home[i]==guest[j]):
            answer+=1
print(answer)
        
      
    

