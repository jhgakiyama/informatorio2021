import csv

MODEL = '"model": "preguntas.pregunta",'


def armarRegistro(fila):
    clave = f'"pk": {int(fila[0])},'
    campos = '"fields": {'
    categoria = f'"categoria": {int(fila[1])}'
    texto = f'"texto": "{fila[2]}",'
    categoria += '}}'

    linea = '{' + MODEL + clave + campos + texto + categoria + ','
    return linea


with open('Preguntascsv.csv',  encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    print("[")
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(armarRegistro(row))
            line_count += 1
    print("]")


