n= int(input("enter the no."))
counter=1
while (n>1):
    if(n%2==0):
        n=n/2
        counter=counter+1

    else:
        n=3*n+1
        counter=counter+1
print(counter)
