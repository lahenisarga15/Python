#python programme for creating a lambda function that returns a square value of a given number
#programme peformed by nisarga lahe
def square(x):
    return(x*x)
print(square(2))


#write a python programme to find whether a given string starts with a given character using lambda
#programme performed by nisarga lahe
starts_with =lambda x: True if x.startswith('p') else False
print(starts_with('python'))
starts_with=lambda x: True if x.startswith('p') else False
print(starts_with('java'))


#python programme to extrat year,month,date,time using lambda
#programme performed by nisarga lahe
import datetime
now=datetime.datetime.now()
print("now")
year=lambda x: x.year
month=lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))
