#python function to find no is prime or not
#programme performed by nisarga lahe
def test_prime(n):
     if (n==1):
         return false
     elif(n==2):
         return true
     else:
          for  x in range (2,n):
            if(n%x==0):
                print("false")
            return("true")
          print(test_prime(num))
test_prime(8)
