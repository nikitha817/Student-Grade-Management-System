def Student_info():
    student ={
        "name": input("Enter your name: ").strip(),
        }
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 100:
                print("Please enter a valid age (0-100)")
                continue
            student["age"] = age
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    student["subjects"] = [
        "Maths", "Science", "English", "History", "Geography"
    ]
    student["marks"] = {}
    for subject in student["subjects"]:
        while True:
            try:
                mark = int(input(f"Enter your {subject} marks: "))
                if mark < 0 or mark > 100:
                    print("Please enter a valid mark (0-100)")
                    continue
                student["marks"][subject] = mark
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return student
def calculate_total(marks):
    total_marks = sum(marks.values())
    return total_marks
def calculate_average(marks):
    average = calculate_total(marks) / len(marks)
    return average
def display_student_info(student):
    average_marks = calculate_average(student["marks"])
    print(student)
    print("\n" + "=" * 55)
    print(f"{'Student Report':^55}")
    print(f"{'=' * 55}\n{'-' * 55}")
    print(f"{student['name']:^55}")
    print("-" * 55)
    print(f"|{'Name':<20}: {student['name']}{"|":^55}")
    print(f"|{'Age':<20}: {student['age']}{"|":^60}")
    print("-" * 55)
    for subject, mark in student["marks"].items():
        print(f"|{subject:<20}: {mark}{"|":^60}")
    print("-" * 55)
    print(f"|{'Average Marks':<20}: {average_marks}{"|":^56}")
    print(f"|{'Total Marks':<20}: {calculate_total(student['marks'])}{"|":^57}")
    print(f"|{'Grade':<20}: {grade(average_marks)}{"|":^61}")

def grade(average):
    if average >= 90:
        return "A"
    elif average >= 85:
        return "B"
    elif average >= 75:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 45:
        return "E"
    elif average < 45:
        return "Fail"
    else:
        return "Invalid Marks"
def main():
    student1 =  Student_info()
    display_student_info(student1)
if __name__ == "__main__":
    main()