def calcular_promedio(notas):
    notas = [float(nota) for nota in notas.split(',')]
    promedio = sum(notas) / len(notas)
    return promedio

lista_alumnos = [
    "marco|67,61,73,76",
    "julio|66,83,79,55",
    "cesar|90,85,94,86",
    "kevin|76,55,43,78",
    "sofia|24,59,38,99",
]

nombre_archivo = "promedios.txt"

with open(nombre_archivo, "w") as archivo:
    for alumno in lista_alumnos:
        nombre, notas = alumno.split('|')
        promedio = calcular_promedio(notas)
        archivo.write(f"{nombre}: {promedio:.2f}\n")

print(f"Promedios guardados '{nombre_archivo}'")
