#to check whether the no is palindrome
#programme performed by nisarga lahe
n=int(input("enter the no:"))
temp=n
rev=0
while(n>0):
      dig=n%10
      rev=rev+10+dig
      n=n//10
if(temp==rev):
      print("the number is a palindrome")
else:
      print("the number is not a palindrome")
