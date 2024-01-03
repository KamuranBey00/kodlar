import math
def tfidf_calculator(text):
    unique_words = list(set(word for sentence in text for word in sentence.split()))
    N = len(text)
    idf_values = [math.log10(N / sum(term in sentence.lower() for sentence in text)) for term in unique_words]
    tfidf_list = []
    for sentence in text:
        tfidf_values = [sentence.split().count(term) * idf for term, idf in zip(unique_words, idf_values)]
        tfidf_list.append(tfidf_values)

    return unique_words, tfidf_list
text = ["duran duran sang wild boys in 1984","wild boys don't remain forever wild","who brought wild flowers","it was john krakauer who wrote in to the wild"]

unique_words, tfidf_list = tfidf_calculator(text)
print(unique_words)
for row in tfidf_list:
    print([round(value, 3) for value in row])