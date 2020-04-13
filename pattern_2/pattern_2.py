n=int(input())
val=65
for i in range(0,n):
    if(i==0):
        print(chr(val))
        val=val+1
    elif(i>0):
        print(str(chr(val))*(i+1))
        val=val+1
