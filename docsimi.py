import math


query = input("Enter the query: ")
document1 = input("Enter document 1: ")
document2 = input("Enter document 2: ")

print("\nQuery:", query)
print("Document 1:", document1)
print("Document 2:", document2)

def term_frequency(term, doc):
    """
    Calculate the term frequency (tf) for a term in a document.
    """
    normalize_term_freq = doc.lower().split()
    term_in_document = normalize_term_freq.count(term.lower())
    len_of_document = float(len(normalize_term_freq))
    normalized_tf = term_in_document / len_of_document
    return normalized_tf

def inverse_document_frequency(term, all_docs):
    """
    Calculate the inverse document frequency (idf) for a term.
    """
    num_docs_with_given_term = sum(1 for doc in all_docs if term.lower() in doc.lower().split())
    if num_docs_with_given_term > 0:
        total_num_docs = len(all_docs)
        idf_val = math.log(float(total_num_docs) / num_docs_with_given_term)  # Logarithmic function
        return idf_val
    else:
        return 0


unique_terms = list(set(query.lower().split() + document1.lower().split() + document2.lower().split()))

print("\nUnique Terms:", unique_terms)


query_tfidf = {}
print("\nTF-IDF weights for Query:")
for term in unique_terms:
    tf = term_frequency(term, query)  # Normalization
    idf = inverse_document_frequency(term, [query, document1, document2])  # Inversion and Logarithmic function
    query_tfidf[term] = tf * idf
    print(f"{term}: {query_tfidf[term]:.4f}")


doc1_tfidf = {}
print("\nTF-IDF weights for Document 1:")
for term in unique_terms:
    tf = term_frequency(term, document1)  # Normalization
    idf = inverse_document_frequency(term, [query, document1, document2])  # Inversion and Logarithmic function
    doc1_tfidf[term] = tf * idf
    print(f"{term}: {doc1_tfidf[term]:.4f}")


doc2_tfidf = {}
print("\nTF-IDF weights for Document 2:")
for term in unique_terms:
    tf = term_frequency(term, document2)  # Normalization
    idf = inverse_document_frequency(term, [query, document1, document2])  # Inversion and Logarithmic function
    doc2_tfidf[term] = tf * idf
    print(f"{term}: {doc2_tfidf[term]:.4f}")


def dot_product(vec1, vec2):
    return sum(vec1[term] * vec2[term] for term in vec1 if term in vec2)

def magnitude(vec):
    return math.sqrt(sum(vec[term] ** 2 for term in vec))


cos_sim1 = dot_product(query_tfidf, doc1_tfidf) / (magnitude(query_tfidf) * magnitude(doc1_tfidf))

cos_sim2 = dot_product(query_tfidf, doc2_tfidf) / (magnitude(query_tfidf) * magnitude(doc2_tfidf))

print("\nCosine Similarity:")
print("Query and Document 1:", cos_sim1)
print("Query and Document 2:", cos_sim2)

if cos_sim1 > cos_sim2:
    print("\nDocument 1 is more similar to the query.")
else:
    print("\nDocument 2 is more similar to the query.")
