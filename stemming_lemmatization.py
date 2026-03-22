import nltk
nltk.download("wordnet") # wordnet: lemmatization işlemi icin gerekli veri tabanı
from nltk.stem import PorterStemmer # stemming için fonksion

# porter stemmer nesnesini olustur
stemmer = PorterStemmer()

words = ["running", "runner", "ran", "runs", "better", "go", "went"]

# kelimelerin stem'lerini buluyoruz, bunu yaparkende porter stemmerin stem() fonksiyonunu kullanıyoruz
stems = [stemmer.stem(w) for w in words]
print(f"Stems: {stems}")

# %%

from nltk.stem import WordNetLemmatizer

lemmatization = WordNetLemmatizer()
words = ["running", "runner", "ran", "runs", "better", "go", "went"]
lemmas = [lemmatization.lemmatize(w, pos="v") for w in words]
print(f"Lemmas: {lemmas}")