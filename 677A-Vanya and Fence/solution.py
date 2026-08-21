n,h=map(int,input().split(" "))
sum=0
a=map(int,input().split(" "))
for i in a:
        if(i<=h):
           sum+=1
        else:
              sum+=2
print(sum)  

  
