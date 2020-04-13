n=int(input())
space=0
val=n
for i in range(0,(n*2)+1):
    if(i<n):
        print(str(("* ")*val)+str((" ")*space)+str(("* ")*val))
        space=space+(2+2)
        val=val-1
    else:
        print(str(("* ")*val)+str((" ")*space)+str(("* ")*val))
        space=space-(2+2)
        val=val+1
       
    
        
    
    
    
