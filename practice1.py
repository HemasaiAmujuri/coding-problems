names_scores=[]
n = int(input("Enter no of students data is listed:"))
for i in range(n):
    name = str(input("Enter name of a student:"))
    score = float(input("Enter scores of a student:")) 
    names_scores.append([name, score])
print(names_scores)

unique_scores = []
seen = set()
for name, score in names_scores:
    if score not in seen:
        unique_scores.append(score)
        seen.add(score)
sorted_unique_scores =sorted(unique_scores)
names_second_lowest = []
for name,score in names_scores:
    if score == sorted_unique_scores[1]:
        names_second_lowest.append(name)
print(names_second_lowest)
sorted_names_second_lowest =sorted(names_second_lowest)
for name in sorted_names_second_lowest:
    print(name)













