text=input().strip()
upper_count=0 
lower_count=0
for i in text:
    if(i.isupper()):
        upper_count+=1 
    if(i.islower()):
        lower_count+=1 
if(upper_count>lower_count):
    print(text.upper())
else:
    print(text.lower())               
  

