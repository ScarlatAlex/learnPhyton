# nums = [1, 2, 10, True, "Hi", 6.1, [2, 4]]
# nums[2] = 3
# print(nums[6][1])
b = [2, 4, 7, 8, 5]
# functia append -adauga numarul la sfarsiut sirului
#         insert adauga un numar ce nu este in sirul indicat
#         extend adauga sirul introdus la sfarsitul sirului initial
#         sort - sortare numerele in crestere
#         reverse - reverseaza ordinea numerelor
#         pop - sterge ultimul element din lista dupa index
#         remove(numar) - sterge numarul la indicarea acestuia
#         clear - sterge toata lista
#         count - numara elemente de acelas tip din lista
#         len - scrie numarul de elemente introduse
numbers = [5, 2, 7]
# numbers[3] = 100
numbers.append(100)
numbers.insert(1, True)
numbers.extend([2, 5, 7, ])
# sau
numbers.extend(b)
numbers.sort()
# numbers.reverse()
# numbers.pop()
# numbers.remove(2)
# numbers.clear()
# print(numbers.count(2))

print(len(numbers))
