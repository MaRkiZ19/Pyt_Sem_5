# def easy_num(num):
#    k=0
#    for i in range(2, num // 2+1):
#     if (num % i == 0):
#         k = k+1
#     if (k <= 0):
#         print("Число простое")
#     else:
#         print("Число не является простым")
# easy_num(int(input(' ')))

a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")