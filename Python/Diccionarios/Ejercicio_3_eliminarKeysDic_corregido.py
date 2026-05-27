#Cree un programa que use una lista para eliminar keys de un diccionario

employee = {
    'nombre' : 'laura',
    'apellido' : 'molina',
    'pais' : 'colombia',
    'ciudad' : 'bogota',
}

deleted_keys = ['pais', 'ciudad']

for key in deleted_keys:
    employee.pop(key)

print(employee)