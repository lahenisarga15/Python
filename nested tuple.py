#Python programme to insert a new element into tuple of element at a specified position
#programme performed by nisarga lahe

names=("nisarga","om","khushi","soham")
list=[input("enter new name: ")]
new= tuple(list)
position=int(input(("enter position no: " )))
names1=names[0:position-1]
names1s=names1+new
names=names1+names[position-1:]
print(names)


#Python programme  to modify the element of tuple
#programme performed by nisarga lahe
num=(1,2,3,4,5,6)
list=[int(input("enter the no"))]
new=tuple(list)
pos=int(input("enter the pos no"))
num1=num[0:pos-1]
num1=num1+new
num=num1+num[pos:]
print(num)


#Python programme to delete an element from a tuple
#Programme performed by nisarga lahe
num=(10,20,30,40,50,60)
pos=int(input("enter the position no"))
num1=num[0:pos-1]
num=num1+num[pos:]
print(num)
