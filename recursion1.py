#python programme to calculate factorial values using recursion
#progrmme performed by nisarga lahe

def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))
   
num=8
print("factorial of ",num,"is",factorial(num))


#python programme to solve fabonacci sequence using recursion
#programme performed by nisarga lahe

def fabonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return (fabonacci(n-1) + (fabonacci(n-2)))
print (fabonacci(7))
