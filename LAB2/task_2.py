import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
print(id(original), id(alias), id(shallow), id(deep))
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print(id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0][1]))

original.append(["Databases", 5])
print(id(original), id(alias), id(shallow), id(deep))
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print(id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0][1]))

original[0][1] = 3
print(id(original), id(alias), id(shallow), id(deep))
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]))
print(id(original[0][1]), id(alias[0][1]), id(shallow[0][1]), id(deep[0][1]))

wrong_matrix = [[0] * 3] * 3
print(wrong_matrix)
print(id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))

wrong_matrix[0][0] = 1
print(wrong_matrix)
print(id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))

correct_matrix = [[0] * 3 for _ in range(3)]
print(correct_matrix)
print(id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))

correct_matrix[0][0] = 1
print(correct_matrix)
print(id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))

