student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last name")
except TypeError:
    print("I can't add these two together!")

print("This code executes!")