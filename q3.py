# Program 3: Marks of 5 subjects, total and average
marks = []
for i in range(5):
    m = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)