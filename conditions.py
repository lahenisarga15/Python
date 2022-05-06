#python programme to use condition (if,else)
#programme performed by nisarga lahe
discount=float(input("enter your discount"))
quantity=int(input("enter your quantity"))
ppi=float(input("enter the ppi"))
if quantity>=1000:
    total=(quantity*ppi)-(quantity*ppi*discount/100)
    print("total expenses = ",total)
else:
    print("sorry no discount")
