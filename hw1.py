# Задача:
# - написать программу при запуске которая выводит Hello world! - 10 раз
# и в следующей строке печает сумму 1 + 10 + '11' (ошибок быть не должно)

hello_world = 'Hello World!'
repeat_times = 10
summ = 1 + 10 + int('11')

print((hello_world + ' ') * repeat_times)
print(summ)
