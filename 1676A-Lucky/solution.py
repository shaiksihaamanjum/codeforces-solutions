n=int(input())
for i in range(n):
    s=input()
    l=[]
    for i in s:
        l.append(int(i))
    if(len(l)==6):
        if(l[0]+l[1]+l[2]==l[3]+l[4]+l[5]):
            print("YES")
        else:
            print("NO")    
       
            

   
       



