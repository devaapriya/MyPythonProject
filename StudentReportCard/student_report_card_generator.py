
print("---------------------------")
print("--  Student Report Card  --")
print("---------------------------")

# student_id = input("Enter student ID ")
# student_name = input("Enter student Name ")
no_of_subjects = int(input("Enter the number of subjects:"))

subject_mark = {}
for num in range(no_of_subjects):
    subject = input(f"Enter Subject {num+1} Name: ")
    mark = int(input(f"Enter the mark (0-100) for {subject}: "))

    while mark > 100 :
        mark = int(input("Please enter a valid mark between 0-100 "))

    subject_mark[subject] = mark
    average = sum(subject_mark.values())/no_of_subjects
    print(average)