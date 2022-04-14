#wpp to reverse the given no
#programme performed by nisarga lahe
n=int(input("enter no"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
    print("reverse the no:",rev)
