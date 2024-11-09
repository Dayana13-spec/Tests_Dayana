numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
skip1 = numbers[5:]
skip2 = numbers[:4]
summ1 = sum(skip1)
lenn = len(numbers)
avarage1 = round(summ1/lenn)
summ2 = sum(skip2)
avarage2 = round(summ2/lenn)
sum_so = summ1 + summ2

soso = round(sum_so/lenn, 2) #арифметическая сумма
numbers[4] = soso
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
