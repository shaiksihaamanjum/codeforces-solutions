n=int(input())
s=input().upper()
if(len(s)==n):
    if(s.count('A')>s.count('D')):
        print("Anton")
    elif(s.count('A')<s.count('D')):
        print("Danik") 
    else:
        print("Friendship") 



    