gradebook = {
    "Alex": "A",
    "Sam": "B",
    "Jordan": "A-"
}

student_name = input("Student name: ")

if student_name in gradebook:
    print(gradebook[student_name])
else:
    print("Student not found.")
