import copy

d = {1: "A", 2: "B", 3: "C"}
print(d[1])
print(d)

d2 = dict(a="A", b="B")
print(d2)

# accessing items in dictionary
print("First key ==>", d[1])
print("First key ==>", d[2])


d3 = {"Name: ": "Silu", "Age: ": 23, "Location: ": "Makola"}
print(d3)
print("Name: ", d3["Name: "])
print("Age: ", d3["Age: "])

d3["Status"] = "Single"
d2["c"] = "C"
d[1] = "C"

# new value assigned
print("d full dictionary with new value: ", d)
print("d2 full dictionary with new value: ", d2)
print("d3 full dictionary with new value: ", d3)

print("-------------------------------------------------------------------update value---------------------------------------------------------------")

# Update value
d[1] = "AAA"
d2['c'] = "D"
d3["Status"] = "Unmarried"
print("d full dictionary with update value: ", d)
print("d2 full dictionary with update value: ", d2)
print("d3 full dictionary with update value: ", d3)

print("--------------------------------------------------------------------delete value--------------------------------------------------------------")

# delete value
del d[1]
d2.pop("c")
print("d full dictionary after delete a value: ", d)
print("d full dictionary after delete a value: ", d2)

print("------------------------------------------------------------------again add value----------------------------------------------------------------")

# again added values to d dictionary
d = {1: "A", 2: "B", 3: "C"}
print("d full dictionary: ", d)

print("-----------------------------------------------------------------clear dictionary-----------------------------------------------------------------")

# clear full dictionary
d.clear()
print("d full dictionary after delete all values: ", d)

print("------------------------------------------------------------------value adding----------------------------------------------------------------")

# again added values to d dictionary
d = {1: "A", 2: "B", 3: "C"}
print("d full dictionary: ", d)

print("-----------------------------------------------------------------for loop-----------------------------------------------------------------")

# iterate all values in d2 dictionary
for key in d3.keys():
    print(key)

for value in d3.values():
    print(value)

for pair in d2.items():
    print(pair)

print("--------------------------------------------------------------nested dictionary--------------------------------------------------------------------")

# nested dictionary
new_dictionary = {1: "Test", "Name: ": "Silu", 3:{1: "A", 2: "B", 3: "C"}}
print("New dictionary:", new_dictionary)
print("New dictionary nested loop:", new_dictionary[3])
print("New dictionary third index:", new_dictionary[3][2])

print("---------------------------------------------------------------coping dictionary/shalow copy -------------------------------------------------------------------")

orginal1 = {"Name: ": "Silu", "Marks: ": 95}
shallow1 = copy.copy(orginal1)
print("orginal: ", orginal1)
print("shallow: ", shallow1)

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99

print("Original:", original)
print("Shallow:", shallow)


