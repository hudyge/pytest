L=[2,8,3,50]
number = 0
temp = 1
for i in L:
    temp *= i
    str_number=str(temp)
    number=str_number.count('0')
    if number:
        temp =str_number[-number]
print(number) 