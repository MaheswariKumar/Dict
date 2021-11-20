#Chapter-6
#Dictionaries
#Simple Dictionaries
person = {"name" : "mahi", "age" : 5}
print(person["name"])
print(person["age"])

#Access the value assoisated with key
new_point = person["age"]
print("congrats you got "+ str(new_point) + " points")

#Adding new key value pair
person["dob"] = "8 april 1998"
person["sister"] = "tamil"
print(person)

#starting with new empty dict
scl = {}
scl["name"] = "JGHS"
scl["count"] = 2566
print(scl)

#Modifiying dict
scl["count"] = 3000
print(scl)

#alien speed
alien = {"x_pos" : 0, "speed" : "fast"}
if alien["speed"] == "slow":
	x_loc = 2
elif alien["speed"] == "medium":
	x_loc = 4
else:
	x_loc = 6

alien["x_pos"] = alien["x_pos"] + x_loc
print("new point " + str(alien["x_pos"]))

#deleting the dict
del scl["count"]
print(scl)

#dict of similar objects
friends = {
	"name1" : "mahi",
	"name2" : "tamil",
	"name3" : "nandi",
}
print(friends)
print("my fav friend is " + 
	friends["name3"].upper())

#Ass-1
details = {"name" : "mahi", "age" : 23, "scl": "JGHS"}
print(details)

#Ass-2
fav_num = {
	"mahi" : 5,
	"tamil" : 7,
	"nandi" : 1
}
print(fav_num)

#Ass-3
glossery = {"word" : "del", "mean" : "deleting the word", "word2" : "pop", "mean2" : "remove"}
print("\n The " + str(glossery["word"]) + " meaning is " + str(glossery["mean"]) + "\n The "+ str(glossery["word2"]) + " meaning is " + str(glossery["mean2"]))

#Looping through dict
for k, v in friends.items():
	print(k + " is " + v)

#Looping through keys():
sisy_name = ["name3"]
for names in friends.keys():
	print(names.title())
	
	if names in sisy_name:
		print("cool!!...your name also added " + names.upper())
	if "name4" not in names:
		print("name4, plz give your name")

#Looping through keys in order:
for detail in sorted(details.keys()):# if you want your keys in order you can you use sorted function
	print(detail.title() + " is one of the detail that we want")

#Looping through values():
for detail in set(details.values()): # if you want values without repeating you can use Set, bcoz set is similar to list which contains unique values only
	print(detail)

#Ass-1
glossery["set"] = "unique representative"
for name, meaning in glossery.items():
	print(name + " : " + meaning)

#Ass-2
rivers = {"kudagu" : "kaveri", "egypth" : "nile", "madurai" : "krishna"}
for city, river in rivers.items():
	print(river.title() + " river running through " + city.upper())
for area in rivers.keys():
	print(area)
for river in rivers.values():
	print(river)

#Ass-3
#list of ppl who are took and not taken the poll
students = {
	"mahi" : "python",
	"tamil" : "css",
	"nandi" : "c++",
}
poll_students = ["mahi", "tamil"]
for student in students.keys():
	if student in poll_students:
		print(student.title() + " thankyou for taking the poll")

if "prithi" not in students.keys():
	print("prithi plz take the poll")

#Nesting - nesting is powerful feature that will help you to insert the list in dic and insert the dic in the list or dic in dic like this
#A lsit of dic  in the list
user1 = {"name" : "mahi", "age" : "23"}
user2 = {"name" : "tamil", "age" : "27"}
user3 = {"name" : "nandi", "age" : "18"}

users = [user1, user2, user3]
for user in users:
	print(user)
#creating empty list
users = []
for uses in range(30):
	new_user = {"name" : "mahi", "age" : "23"}
	users.append(new_user)

for user in users[:5]:
	print(user)
print("------")
print("totaly created user count is " + str(len(users)))

for user in users[:3]:
	if user["name"] == "mahi":
		user["name"] = "prithi"
		user["age"]  = 2
		print(user)

#A list of values in dict
ice_cream = {
	"cone" : "icone",
	"flavour" : ["choco", "vennila"]
}
print("you ordered " + str(ice_cream["cone"]) + " with the following flavour:")
for flavour in ice_cream["flavour"]:
	print(flavour)

program_languages = {
	"mahi" : ["python", "ML"],
	"nandi" : ["ruby"],
	"tamil" : ["c" , "++"],
	"prithi" : ["C"]
}
for n, l in program_languages.items():
	if len(l) > 1:
		print(str(n) + "'s fav language is: ")
		for language in l:
			print("\t" + language)
	elif len(l) == 1:
		for language in l:
			print(str(n) + "'s fav language is: " + str(language))

#nested dict inside dict
users = {
	"mahi" : {
	"1st_name" : "mahi",
	"2nd_name" : "kumar",
	"age" : "23",
	},

	"tamil" : {
	"1st_name" : "tamil",
	"2nd_name" : "kumar",
	"age" : "27",
	},
}
for user_name, user_info in users.items():
	print("username : " + user_name)
	full_name = user_info["1st_name"] + " " + user_info["2nd_name"]
	age = user_info["age"]

	print("\t" + full_name)
	print("\t" + age)

#Ass-1
user1 = {"name" : "mahi", "age" : 23}
user2 = {"name" : "tamil", "age" : 27}

users = [user1, user2]
for user in users:
	print(user)

#Ass-2
pet1 = {"owner" : "kumar" , "pet" : "cat"}
pet2 = {"owner" : "sumathi" , "pet" : "dog"}
pet3 = {"owner" : "prithi" , "pet" : "parrot"}

pets = [pet1, pet2, pet3]
for pet in pets:
	print(pet)

#Ass-3
fav_places = {
	"mahi" : ["kochin", "maldives", "hyd"],
	"tamil" : ["delhi"],
	"nandi" : ["kerala", "bangalore"],
	"prithi" : ["home"],
}
fav_places["tamil"] = ["madura"]
for name, place in fav_places.items():
	if len(place) > 1:
		print(str(name) + "'s fav place are: ")
		for pl in place:
			print(pl)
	if len(place) == 1:
		for pl in place:
			print("\n" + str(name) + "'s fave place is : " + str(pl) + "\n")

#Ass-4
fav_numbers = {
	"mahi" : [1, 5, 6] ,
	"tamil" : [3],
	"nandi" : [4, 6],
	"prithi" : [4],
}
for name, numbers in fav_numbers.items():
	print(str(name) + "'s fav number is: ")
	for number in numbers:
		print("\t" + str(number))

#Ass-5
cities = {
	"salem" : {
	"state" : "tamilnadu",
	"population" : 70,
	"fact" : "special for mango",
	},

	"trichi" : {
	"state" : "tamilnadu",
	"population" : 50,
	"fact" : "special for college",
	}
}
for city_place, city_info in cities.items():
	print("city name: " + str(city_place))
	state = city_info["state"]
	population = city_info["population"]
	fact = city_info["fact"]
	print("\t" + "state : " + str(state))
	print("\t" + "population : " + str(population))
	print("\t" + "fact : " + str(fact))