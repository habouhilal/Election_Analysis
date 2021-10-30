#print hello world first python code 
print ("hello world")

#create list python 
counties = ["Arapahoe","Denver","Jefferson"]

#print the list 
counties

#print one element of the list using index 
counties[0]
print(counties[2])

#get the lenght on the list 
len(counties)

#print a range from the list 
counties[0:1]
counties[0:2]
counties[0:3]

#add intem to the list 
counties.append("El Paso")
counties
counties.insert(1,"El Paso")
counties

# remove item from the list 
counties.remove("El Paso")
counties

#remove last instance of item from the list 
counties.pop(3)

#change an element of the list
counties[2] = "El Paso"
counties

#create dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict

#add other value to the dictionary 
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict

#printing only keys 
counties_dict.keys()

#ptinting the values
counties_dict.values()

#get a specific value 
counties_dict.get("Denver")

# create voting list of dictionaries
voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data

voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
voting_data

#voting_data.remove({'county':"Arapahoe", "registered_voters": 422829)


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.
percentage_votes = int((my_votes / total_votes) * 100)
print("I received " + str(percentage_votes)+"% of the total votes.")

# practice if statement 
counties1 = ["Arapahoe","Denver","Jefferson"]
if counties1[1] == 'Denver':
    print(counties1[1])

#oractice else if 
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

#Membership operation 
counties2 = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties2:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#logicaloperations
if "Arapahoe" in counties2 and "El Paso" in counties2:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# Loops
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#key to get the keys
for county in counties_dict.keys():
    print(county)

# values method 
for voters in counties_dict.values():
    print(voters)

#item method 
for county, voters in counties_dict.items():
    print(county , voters)

#list of dictionary 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#get the value of a list of the dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Print() Fuction
 print("Arapahoe and Denver are not in the list of counties.")

 #f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#f-string with dictionnaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

# Activity  print each county and registred voters   
county_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in county_dict.items():
    print(f"{county} county has {voters} registered voters.")

print (county_dict["Denver"])
print (county_dict.keys())
print (county_dict.values())

#using dictionary to do same activity 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")
    