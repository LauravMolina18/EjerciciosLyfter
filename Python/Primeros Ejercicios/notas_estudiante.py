counter_grade = 1
approved_grades = 0
desapproved_grades = 0 
average_approved = 0 
average_desapproved = 0 
total_average = 0 

total_grades = int(input("Ingrese la cantidad de notas: "))
while counter_grade <= total_grades:
    print(f"Nota numero {counter_grade}")
    actual_grade = int(input("Ingrese la nota actual: "))
    if actual_grade < 70:
        desapproved_grades += 1
        average_desapproved += actual_grade
    else:
        approved_grades += 1        
        average_approved += actual_grade
    total_average += actual_grade / total_grades
    counter_grade += 1

if (desapproved_grades > 0):
    average_desapproved = average_desapproved / desapproved_grades
else:
    average_desapproved = 0

if (approved_grades > 0):
    average_approved = average_approved / approved_grades
else:
    average_approved = 0

print(f"El estudiante tiene esta cantidad de aprobadas: {approved_grades}\nEste es el promedio de notas aprobadas: {average_approved}\nEl estudiante tiene esta cantidad de notas desaprobadas: {desapproved_grades}\nEste es el promedio de notas desaprobadas: {average_desapproved}\nEste es el promedio total: {total_average}")
