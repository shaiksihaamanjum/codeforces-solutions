n=int(input())
an=[]
bn=[]
sum_list=[]
for i in range(n):
    a,b=map(int,input().split())
    an.append(a)
    bn.append(b)
sum=0
if(an[0] ==0 & bn[0]==0):
    sum=an[0]+bn[0]
    sum_list.append(sum)
    for i in range(1,n):
        sum_i=an[i]+bn[i]
        sum=sum-an[i]+bn[i]
        sum_list.append(sum)
print(max(sum_list))        






