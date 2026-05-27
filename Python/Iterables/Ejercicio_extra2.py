#Cree un programa que verifique si todos los elementos de una lista son positivos

my_list=[2, 3, 4, 5, -1, -4, 8, 1, 6, -2, 0, 0, -7]

counter = 0 

for numbers in my_list: 
    if numbers <= 0:
        counter  = counter+1
        
print(f'Hay al menos {counter} números negativos o 0 en esta lista')
