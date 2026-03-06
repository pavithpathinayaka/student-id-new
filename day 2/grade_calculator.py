# ...existing code...

while True:
    # ask for student name
    name = input("Enter student's name (or type Exit to quit): ")
    if name.strip().lower() == 'exit':
        break

    # ask for three subject marks
    marks = []
    for i in range(1, 4):
        while True:
            try:
                m = float(input(f"Enter mark for subject {i}: "))
                marks.append(m)
                break
            except ValueError:
                print("Please enter a numeric value.")

    # calculate average
    average = sum(marks) / len(marks)

    # determine grade
    if average >= 75:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 40:
        grade = 'C'
    else:
        grade = 'Fail'

    # display result in clean formatted block
    print("\n" + "-" * 30)
    print(f"Name   : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {grade}")
    print("-" * 30)

print("Exiting program.")