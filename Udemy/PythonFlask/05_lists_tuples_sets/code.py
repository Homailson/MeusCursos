l = ["Bob", "Rolf", "Anne"] # a lista é mutável e pode ser indexável
t = ("Bob", "Rolf", "Anne") # a tupla é imutável, não se pode adicionar ou remover elementos. Porém é indexável
s = {"Bob", "Rolf", "Anne"} # o conjunto (set) não possui uma ordem para seus elementos e eles não se repetem
print(l[0])
print(t[1])

l.append("Jane")
l.remove("Bob")

s.add("João")

print(s)