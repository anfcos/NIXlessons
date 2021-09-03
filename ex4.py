#Дан список из строк. Создайте однострочное решение (при помощи list comprehension), которое приведёт 
# к верхнему регистру все строки, содержащие слово 'price')
isfile = input()
file = open(isfile, 'r+')
las = [line.strip().upper()  for line in file.readlines() if 'price' in line ]
print(las)
file.close()