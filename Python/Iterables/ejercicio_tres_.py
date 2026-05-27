#Cree un programa que intercambie el primer y ultimo elemento de una lista

numbers=[2, 4, 6, 8, 10, 12]
temp=numbers[0]
numbers[0]=numbers[len(numbers) -1]
numbers[len(numbers) -1] = temp

print(numbers)

