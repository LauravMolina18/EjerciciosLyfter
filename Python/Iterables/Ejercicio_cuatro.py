#Cree un programa que elimine todos los números impares de una lista.
numbers=[10, 11, 12, 13, 14, 15, 16, 17, 18]

deleted_number = []

for index in range(len(numbers) -1, -1, -1):
    if numbers[index] % 2 != 0:
        deleted_number.append(numbers.pop(index))
        
print(numbers)
print(f'Deleted numbers: {deleted_number}')
