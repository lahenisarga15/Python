#python programme to find max of three numbers
#programme performed by nisarga lahe
def maximum(a,b,c):
    
    if(a>=b) and(a>=c):
        maximum=a
    elif (b>=a) and (b>=c):
         maximum=b
    else:
         maximum =c
    return maximum
a=12
b=16
c=24
print(maximum(a,b,c))
maximum
