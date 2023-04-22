# Task1. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в 
# целую степень B с помощью рекурсии.

# def degree(a,b):
#     if b==1: return a
#     else: return a*degree(a,b-1)

# a = int(input("A = "))
# b = int(input("B = "))
# print(degree(a,b))

# Task2. Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a,b):
    if b==0: return a
    else: return 1+sum(a,b-1)

a = int(input("a = "))
b = int(input("b = "))
print(sum(a,b))