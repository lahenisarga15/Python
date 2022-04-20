def avg(*n):
    for i in n:
        sum=0
        sum = sum+i
        avg=sum/len(n)
        print(avg)

#function calling
avg(10,20,30,40,50,60)
