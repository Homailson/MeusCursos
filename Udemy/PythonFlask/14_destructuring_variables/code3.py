# Desconstruindo uma lista em duas partes: início e fim
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)


# Desconstruindo uma lista em duas partes: início e fim
*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)


# Desconstruindo uma lista em três partes: início, meio e fim
head, *mid, tail = [1, 2, 3, 4, 5]

print(head)
print(mid)
print(tail)

