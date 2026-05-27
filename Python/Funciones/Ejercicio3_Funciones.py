#Cree una función que retorne la suma de todos los números de una lista.

def sum_numbers(my_list):
   total = 0

   for number in my_list:
      total =  total + number
   return total

my_list = [2, 4, 5, 6, 8, 7]
result = sum_numbers(my_list)
print(result)

