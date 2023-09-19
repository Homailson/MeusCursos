amigos = ["Rolf", "Jen", "Bob", "Anne"]

for amigo in amigos:
    print(f"{amigo} é meu amigo(a)")

for amigo in range(4):
    print(f"{amigo} é meu amigo(a)")


grades = [35, 67, 98, 100, 100]
amount = len(grades)
total = 0

for grade in grades:
    total += grade
print(f"The mean of grades is {total/amount}")