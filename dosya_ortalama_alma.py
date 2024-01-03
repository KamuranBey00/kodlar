fhandle = open("textfile.txt", "r")
for line in fhandle:
    line = line.strip()
    name, grades = line.split(":")
    grade_list = grades.split(",")
    sum= 0
    for grade in grade_list:
        sum += int(grade)
    avg = sum/len(grade_list)
    print(name + "\t" + str(avg))

