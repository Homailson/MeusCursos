# Diferença entre dois conjuntos
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = abroad.difference(friends)
print(local_friends)


# União entre dois conjuntos
all_friends = friends.union(local_friends)
print(all_friends)


# Intersecção entre dois conjuntos
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both =  art.intersection(science)

print(both)