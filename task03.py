# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



num=[1,3,2,3,3,4,5,5] 
min_num=min(num)
max_num=max(num)
for i in range(len(num)):
    if num[i]==max_num:
        num[i]=min_num
print(num)
