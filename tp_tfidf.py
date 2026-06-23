import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import pandas as pd

corpus = [
    "Python is an interpreted and high-level language while CPlus is a compiled and low-level language",
    "JavaScript runs in web browsers while Python is used in various applications including data science and artificial intelligence",
    "JavaScript is dynamically and weakly typed while Rust is statically typed and ensures greater data security",
    "Python and JavaScript are interpreted languages while Java CPlus and Rust require compilation before execution",
    "JavaScript is widely used in web development while Go is ideal for servers and cloud applications",
    "Python is slower than CPlus and Rust due to its interpreted nature",
    "JavaScript has a strong ecosystem with Nodejs for backend development while Python is widely used in data science",
    "JavaScript does not require compilation while CPlus and Rust require code compilation before execution",
    "Python and JavaScript have large communities and an extensive number of available libraries",
    "Python is ideal for beginners while Rust and CPlus are more suitable for experienced programmers"
]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(corpus)

vocabulary = vectorizer.get_feature_names_out()

print("\\nVOCABULARIO:")
print(vocabulary)

df_tfidf = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vocabulary
)

print("\\nMATRIZ TF-IDF:")
print(df_tfidf)

all_words = []

for texto in corpus:
    all_words.extend(texto.lower().split())

word_freq = Counter(all_words)

top10 = word_freq.most_common(10)

words = [x[0] for x in top10]
freqs = [x[1] for x in top10]

plt.figure(figsize=(10, 5))
plt.bar(words, freqs)

plt.title("Top 10 Palabras Más Frecuentes")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
