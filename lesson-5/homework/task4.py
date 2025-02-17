import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(name, students, tuition):
    names = [item[0] for item in universities]
    students = [item[1] for item in universities]
    tuition = [item[2] for item in universities]
    mean_students = statistics.mean(students)
    median_students = statistics.median(students)
    mean_tuition = statistics.mean(tuition)
    median_tuition = statistics.median(tuition)


    
    print("**********************************")
    print(f"Total students: {sum(students):,}")
    print(f"Total tuition: $ {sum(tuition):,}")
    print("                                  ")
    print(f"Student mean: {mean_students:,.2f}")
    print(f"Student mean: {median_students:,}")
    print("                                  ")
    print(f"Student mean: $ {mean_tuition:,.2f}")
    print(f"Student mean: $ {median_tuition:,}")
    print("**********************************")

    

enrollment_stats("names", "students", "tuition")