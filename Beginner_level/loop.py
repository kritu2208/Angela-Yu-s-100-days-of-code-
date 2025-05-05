stu_heights = input("what is the height of the student?").split()
for n in range(0, len(stu_heights)):
    stu_heights[n] = int(stu_heights[n])
print(stu_heights)

total_heights = 0 
for heights in stu_heights:
    total_heights += heights  
print(total_heights)
number_stu = 0
for student in stu_heights:
    number_stu += 1
print(number_stu)    
highest_height = 0
for height in stu_heights:
    height > highest_height
    highest_height = height
print(highest_height)