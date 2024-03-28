student_marks = {}
n=int(input("ENTER THE NUMBER OF STUDENTS:"))
for i in range(n):
    name = str(input("ENTER NAME OF A STUDENT:"))
    marks= list(map(int,input().split()))            
    student_marks[name] = marks
print(student_marks)
search_name = str(input("Enter name of a student "))
if search_name in student_marks:
    marks = student_marks[search_name]
    average = sum(marks)/len(marks)
    print(average)



# student_marks = {}
# n = int(input())
# for i in range(n):
#     name_marks = input()
#     name, marks_str = name_marks.split(maxsplit=1)  # Split only once
#     marks = [float(x) for x in marks_str.split()]             
#     student_marks[name] = marks

# search_name = input()
# if search_name in student_marks:
#     marks = student_marks[search_name]
#     average = sum(marks) / len(marks)
#     formatted_average = "{:.2f}".format(average)
#     print(formatted_average)