n=int(input())
count=0 
for i in range(n):
         values=list(map(int,input().split()))
         if(values[0]+values[1]+values[2]>=2):
                 count+=1

print(count)

                        
    

       
        
