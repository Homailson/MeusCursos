friend_ages = {"Rolf":24
              ,"Ana":45
              ,"Marcos":27
              ,"Antonio":38
}

for i,j in friend_ages.items():
    print(i, j)

# Lista de dicionários

amigos = [
     {"name": "Jose", "age":21}
    ,{"name": "Maria", "age":25}
    ,{"name":"Mateus", "age":19}
    ,{"name":"Judas", "age":31}
    ,{"name":"Paulo", "age":24}
]

print(amigos)

print(amigos[0]["name"])

student_attendance = {"Rolf":96,"Ana":80,"Marcos":90}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Rolf" in student_attendance:
    print(f"Rolf: {student_attendance['Rolf']}")
else:
    print("Rolf is not a student in this class.")

attendance_values = student_attendance.values()

print(sum(attendance_values)/len(attendance_values))

# Meu dicionário e treino com ele

jogos_favoritos = {"Phantasy Star": 1987,
                   "Sonic 1": 1991,
                   "Resident Evil 4": 2005,
                   "Resident Evil 1": 1996,
                   "Resident Evil Code Veronica": 2000,
                   "Resident Evil 3": 1999,
                   "Valorant": 2020,
                   "Guardians Crusade": 1998,
                   "Metal Gear Solid": 1998
}

print(jogos_favoritos.keys())
print(jogos_favoritos.values())

for nome, ano_lancamento in jogos_favoritos.items():
    print(f"{nome} é um dos meus jogos favoritos e foi lançado em {ano_lancamento}")