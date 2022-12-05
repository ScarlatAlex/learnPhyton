# # functia pass - nu reda nimic pe ecran
# def testFunc(word):
#     print(word, end="")
#     print("!")
#     # pass
#
#
# testFunc("Hi")
#
#
# # testFunc(5)
# # testFunc(3.5) - tot ce se introduce in (), se va printa corect

# def summa(a, b):
#     # res = a + b
#     return a + b
#
#
# res = summa(5.2, 7)
# print(res)
# print(summa("H", "i"))

# Identifica elementul minimal din sirul dat
# # ex 1
# num1 = [5, 7, 8, 5, 2]
# min = num1[0]
# for el in num1:
#     if el < min:
#         min = el
# print(min)

# # ex 2
# num2 = [2.3, 4.5, 1.9, 5.8, 2.21]
# min = num2[0]
# for el in num2:
#     if el < min:
#         min = el
# print(min)

# utilizam functii pentru simplificarea codului
def minimal(l):
    minNumber = l[0]
    for el in l:
        if el < minNumber:
            min = el
    return minNumber


num1 = [5, 7, 8, 5, 2]
min1 = minimal(num1)

num2 = [2.3, 4.5, 1.9, 5.8, 2.21]
min2 = minimal(num2)

if min1 < min2:
    print(min1)
else:
    print(min2)

# lambda - functii anonime
# def summa(x,y):
#     return x * y   - utilizam:
func = lambda x, y: x * y
res = func(5,6)
print(res)