s1=input()
s2=input()
s1=list(sorted(s1.lower()))
s2=list(sorted(s2.lower()))
if(s1==s2):
    print("it is anagram")
else:
    print("not a anagram")
