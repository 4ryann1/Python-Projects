
#Taking Student Information
student_name = input("Enter Student Name: ")
r_no = int(input("Enter Student Number: "))

#Taking Student Marks of Maths, SSt, Science
mathematics = int(input("Enter Marks (Mathematics): "))
social_science = int(input("Enter Marks (Social Science): "))
physics = int(input("Enter Marks (Physics): "))
chemistry = int(input("Enter Marks (Chemistry): "))
biology = int(input("Enter Marks (Biology): "))

total_obtained_marks = mathematics + social_science + physics + chemistry + biology
total_marks = 500

average_marks = total_obtained_marks / total_marks
percentage_obtained = average_marks * 100

if percentage_obtained >=90 and percentage_obtained<= 100:
    print(f"Grade A. You obtained {percentage_obtained}.+")
elif percentage_obtained >=80 and percentage_obtained<= 89:
    print(f"Grade A. You obtained {percentage_obtained}.")
elif percentage_obtained >=70 and percentage_obtained<= 79:
    print(f"Grade B. You obtained {percentage_obtained}.")
elif percentage_obtained >=60 and percentage_obtained<= 69:
    print(f"Grade C. You obtained {percentage_obtained}.")
elif percentage_obtained >=50 and percentage_obtained<= 59:
    print(f"Grade D. You obtained {percentage_obtained}.")
elif percentage_obtained < 50:
    print(f"Grade F. You obtained {percentage_obtained}.")
elif mathematics>=35 and biology>=35 and social_science>=35 and chemistry>=35 and physics>=35:
    print("You Passed!")
else:
    print("Sorry! Try Next Year")


print("-"*100)
print("-"*100)
print("DR. D. Y. PATIL TECHNICAL CAMPUS, VARALE, TALEGAON DABHADE, PUNE")
print("-"*100)
print("-"*100)

print("Student Details:")
print("Student Name: ", student_name, "Roll No.:", r_no)
print(f"\nMarks of {student_name} are:")
print(f"{'Sr.No.':<8}| {'Subject Name':<16}| {'Marks Obtained':<16}| {'Total Marks':<12}")
print("-" * 58)

# Data rows matching the same column widths
print(f"{1:<8}| {'Mathematics':<16}| {mathematics:<16}| {100:<12}")
print(f"{2:<8}| {'Social Science':<16}| {social_science:<16}| {100:<12}")
print(f"{3:<8}| {'Physics':<16}| {physics:<16}| {100:<12}")
print(f"{4:<8}| {'Chemistry':<16}| {chemistry:<16}| {100:<12}")
print(f"{5:<8}| {'Biology':<16}| {biology:<16}| {100:<12}")