s=(input("enter string"))
s=s.lower()
i=0
j=len(s)-1

while(i<=j):
    if(s[i]==s[j]):
        count=1
    else:
        count=0
        break
    i+=1
    j-=1
if(count==1):
    print("palindrome")
else:
    print("not palindrome")
    
        
    