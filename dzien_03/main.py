# # zip() -> iteracja przez dwie listy, kończy zwracanie elementów jak skończy się najkrótsza lista!

# l1 = [1, 2, 3, 4, 5] # 5 cyfr
# l2 = [literka for literka in "abcdefghij"] # 10 znaków

# print("zip():")
# for el1, el2 in zip(l1, l2):
#     print(el1, el2)

# # zip_longest -> idziemy przez wiele list, dopóki nie skończy się najdłuższa
# from itertools import zip_longest

# print("zip_longest():")
# for el1, el2 in zip_longest(l1, l2):
#     print(el1, el2)


# # cykl
# from itertools import cycle

# print("cycle():")
# for n, el1 in enumerate(cycle(l1)):
#     print(n, el1)
#     if n >= 100:
#         break


# # uczniowie kolejno odlicz do dwóch :)
# print("cycle() i zip()")
# for el1, el2 in zip(l2, cycle([1, 2])):
#     print(el1, el2)


# iloczyn wielu list
# from itertools import product

# l1 = [1, 2, 3, 4, 5]
# l2 = ["a", "b", "c"]
# l3 = ["Jan", "Marysia", "Basia", "Zdzisław"]
# print(list(product(l1, l2, l3)))
