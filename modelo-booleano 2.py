import nltk
from nltk.tokenize import word_tokenize
import string

# Documentos
documentos = {
    "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
    "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
}

# Función para tokenizar y limpiar texto
def limpiar_texto(texto):
    tokens = word_tokenize(texto.lower(), language="spanish")
    tokens_limpios = [
        palabra for palabra in tokens
        if palabra not in string.punctuation
    ]
    return tokens_limpios

# Crear índice invertido
indice = {}

for doc_id, texto in documentos.items():
    palabras = limpiar_texto(texto)

    for palabra in palabras:
        if palabra not in indice:
            indice[palabra] = set()

        indice[palabra].add(doc_id)

# Función de búsqueda booleana
def buscar(consulta):
    consulta = consulta.lower().split()

    if "and" in consulta:
        i = consulta.index("and")
        t1 = consulta[i - 1]
        t2 = consulta[i + 1]

        return indice.get(t1, set()) & indice.get(t2, set())

    elif "or" in consulta:
        i = consulta.index("or")
        t1 = consulta[i - 1]
        t2 = consulta[i + 1]

        return indice.get(t1, set()) | indice.get(t2, set())

    elif "not" in consulta:
        i = consulta.index("not")
        t1 = consulta[i - 1]
        t2 = consulta[i + 1]

        return indice.get(t1, set()) - indice.get(t2, set())

    else:
        return indice.get(consulta[0], set())

# Menú principal
while True:
    consulta = input(
        "\nIngrese una consulta booleana (o 'salir' para terminar): "
    )

    if consulta.lower() == "salir":
        print("Programa finalizado.")
        break

    resultado = buscar(consulta)

    print("Documentos encontrados:", resultado)
    