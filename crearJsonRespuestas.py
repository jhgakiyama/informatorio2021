import csv

MODEL = '"model": "preguntas.respuesta",'

# pregunta_id,id,correcta,texto


def armarRegistro(fila):
    clave = f'"pk": {int(fila[1])},'
    fields = '"fields": {'
    pregunta = f'"pregunta_id": {fila[0]},'
    texto = f'"texto": "{fila[3]}",'
    correcta = f'"correcta": "{fila[2]}"'
    correcta += '}},'

    linea = '{' + MODEL + clave + fields + texto + pregunta + correcta
    return linea


with open('Respuestas.csv',  encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    print("[")
    for row in csv_reader:
        print(armarRegistro(row))
        line_count += 1
    print("]")


