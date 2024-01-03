import math
from collections import Counter

def tfidf(text):
    # Step 1: Tokenize and get unique terms
    sentences = [sentence.split() for sentence in text]
    terms = list(set([term for sentence in sentences for term in sentence]))

    # Step 2: Calculate idf for each term
    N = len(text)
    idf = {term: math.log10(N / sum(1 for sentence in text if term in sentence)) for term in terms}

    # Step 3: Calculate tfidf values for each sentence
    tfidf_values = []
    for sentence in sentences:
        tf = Counter(sentence)
        tfidf_sentence = [tf[term] * idf[term] if term in tf else 0.0 for term in terms]
        tfidf_values.append(tfidf_sentence)

    return terms, tfidf_values

text = ["duran duran sang wild boys in 1984",
        "wild boys don't remain forever wild",
        "who brought wild flowers",
        "it was john krakauer who wrote in to the wild"]

terms, tfidf_values = tfidf(text)

# Output
print(terms)
for values in tfidf_values:
    print([round(val, 3) for val in values])
