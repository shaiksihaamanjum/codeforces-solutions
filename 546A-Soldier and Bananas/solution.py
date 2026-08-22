k,n,w=map(int,input().split())
cost=0 
ask=0
for i in range(1,w+1):
    cost+=(i*k)
if(n<cost):
    ask=cost-n 
    print(ask)
else:
    print(0)        

    
   