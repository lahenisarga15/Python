#wpp to print odd no within the given range
#programme performed by nisarga lahe
lower=int(input("enter the lower limit of the range "))
upper=int(input("entr the upper limit of the range"))
for i in range (lower,upper+1):
    if(i%2!=0):
        print(i)
