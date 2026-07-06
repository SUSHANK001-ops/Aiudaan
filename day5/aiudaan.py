print("Welcome to DPLMS student Registration system")
courses = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

for course in courses:
    print(course)

name = input("Enter your name: ")
email = input("Enter your email: ")
Age = input("Enter your age: ")
Selected_course = input("Enter your selected course: ")

Student_info = {
    "Name": name,
    "Email": email,
    "Age": Age,
    "Selected Course": Selected_course
}
if Selected_course in courses:
    print("Student Registration Successful!")
    print("Student Information:")
    for key, value in Student_info.items():
        print(f"{key}: {value}")
else:
    print("Selected course is not available. Please choose a valid course.")

print("\nStudent Registration Information:")
print(f"Name: {Student_info['Name']}")
print(f"Email: {Student_info['Email']}")
print(f"Age: {Student_info['Age']}")
print(f"Selected Course: {Student_info['Selected Course']}")
