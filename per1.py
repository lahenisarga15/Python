#prgramme performed to calculate total fees
#programme performed by nisarga lahe
totalfees=int(input("enter your fees"))
percent=float(input("enter your percent"))

if percent>= 90 and percent<100:
    totalfees =(fees - fees*80/100)
    
if percent>=80 and percent<90:
    totalfees =(fees-fees *70/100
                
if percent>=70 and percent<80:
    totalfees=(fees-fees*60/100)
else:
    print("no discout")
