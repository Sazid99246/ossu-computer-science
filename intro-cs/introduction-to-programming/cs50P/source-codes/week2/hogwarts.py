students = [
    {"name":"Hurmaione", "house":"Gryffindor", "patronus":"Other"},
    {"name":"Hary", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel terrior"},
    {"name":"Drako", "house":"Slytherin", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")