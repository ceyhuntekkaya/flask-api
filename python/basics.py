from datetime import datetime;

# ct stores current time
ct = datetime.datetime.now()
print("current time:-", ct)

# ts store timestamp of current time
ts = ct.timestamp()
print("timestamp:-", ts)
name = "Ceyhun"
full_name = f"Person: {name}"
print(full_name)

geetring = "Hello, {}".format(name)
print(geetring)

# age = int(input("Your age:"))
# print(f"Your age id {age:.2f}")

l = ["a","b","c"]
t = ("a","b","c")
s = {"a","b","c"}

friends = {"Canan", "Aslı", "Gamze"}
abroad = {"Canan", "Gamze"}
print(friends.difference(abroad))          
print(friends.union(abroad))      
print(friends.intersection(abroad))        


numbers = [1,3,5]
double = [num *2 for num in numbers]
print(double)


cities = ["Adana","Kayseri","Konya","Ankara","Adıyaman"]
filtered_cities = [city for city in cities if city.startswith("A")]
print(filtered_cities)



head, *tail = [1,2,3,4,5]