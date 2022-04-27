#Python script to add key in a dictionary
#Programme performed by nisarga lahe
d={0:10,1:20}
print(d)
d.update({2:30})
print(d)


#Python script to concatinate the following dictionries to create the new one
#Programme performed by nisarga lahe
dict1={1:20,2:30}
dict2={3:40,4:50}
dict3={5:60,6:70}
dict4={}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)


#Python programme to delete an  element from the dictionary
#Programme performed by nisarga lahe
mydict={"a":2,"b":4,"c":6,"d":8}
print(mydict)
if "a" in mydict:
    del mydict["a"]
    print(mydict)
