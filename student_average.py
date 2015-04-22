#!/usr/bin/python

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!

def average(numbers):
     total=0
     total=sum(numbers)
     float(total)
     total = total / float(len(numbers))
     return total
    
    
def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    
    
def get_letter_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"
                
        

    
def get_class_average(students):
    results = []
    for student in students:
        studentAvg = get_average(student)
        results.append(studentAvg)
    return average(results)

classroom = [lloyd, alice, tyler]

print "Name:\tLloyd\t\t%.2f" % get_average(lloyd)
print "Name:\tAlice\t\t%.2f" % get_average(alice)
print "Name:\tTyler\t\t%.2f" % get_average(tyler)
print "Classroom:\t\t%.2f" % get_class_average(classroom)







