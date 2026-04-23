ihmiset = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}


print(ihmiset["John"][0], ihmiset["John"][1])
print(ihmiset["Emily"][2])


ihmiset["Anna"][2] = "Teacher"
ihmiset["James"] = ["James", 28, "Writer"]

ihmiset["Sophia"] = ["Sophia", 35, "Doctor"]

del ihmiset["Emily"]

print(ihmiset)