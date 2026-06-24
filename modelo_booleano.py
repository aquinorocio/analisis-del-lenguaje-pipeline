import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('punkt_tab')

# Documentos
documentos = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}

# Función para tokenizar y limpiar los documentos
def limpiar_texto(texto):
    tokens = word_tokenize(texto.lower())
    return [token for token in tokens if token.isalnum()]

# Crear índice invertido
indice_invertido = defaultdict(set)

for doc, texto in documentos.items():
    palabras = limpiar_texto(texto)

    for palabra in palabras:
        indice_invertido[palabra].add(doc)

# Función de búsqueda booleana
def busqueda_booleana(consulta):
    partes = consulta.lower().split()

    if len(partes) != 3:
        return set()

    termino1, operador, termino2 = partes

    if operador == "and":
        return indice_invertido.get(termino1, set()) & indice_invertido.get(termino2, set())

    elif operador == "or":
        return indice_invertido.get(termino1, set()) | indice_invertido.get(termino2, set())

    elif operador == "not":
        return indice_invertido.get(termino1, set()) - indice_invertido.get(termino2, set())

    return set()

# Menú principal
while True:
    consulta = input("Ingrese una consulta booleana (o 'salir' para terminar): ")

    if consulta.lower() == "salir":
        print("Programa finalizado.")
        break

    resultado = busqueda_booleana(consulta)
    print("📄 Documentos encontrados:", resultado)
    