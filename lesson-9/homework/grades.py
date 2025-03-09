import csv

with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    
    data = list(reader)  # Read all rows into a list

    math_list = []
    eng_list = []
    hist_list = []
    science_list = []
    physics_list = []
    
    # Processing math scores
    for row in data:
    
        math_list.append(int(row[1]))
    a = sum(math_list) / len(math_list)
    
    # Processing English scores
    for row in data:
        eng_list.append(int(row[2]))
    b = sum(eng_list) / len(eng_list)
    # Processing History scores
    for row in data:
        hist_list.append(int(row[3]))
    c = sum(hist_list) / len(hist_list)
    # Processing Science scores
    for row in data:
        science_list.append(int(row[4]))
    d = sum(science_list) / len(science_list)
    # Processing Physics scores
    for row in data:
        physics_list.append(int(row[5]))
    e = sum(physics_list) / len(physics_list)


    with open ("average_grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average"])
        writer.writerow([headers[1], a])
        writer.writerow([headers[2], b])
        writer.writerow([headers[3], c])
        writer.writerow([headers[4], d])
        writer.writerow([headers[5], e])

print("Average grades successfully written to 'average_grades.csv'.")
