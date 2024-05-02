n=int(input())
for i in range(0,n+1):
    print(i)
    if(i%3==0 and i%5==0):
        print("fizz buzz")
    elif(i%3==0 and i%5!=0):
        print("fizz")
    elif(i%3!=0 and i%5==0):
        print("buzz")
    else:
        print(i)
        

        
        