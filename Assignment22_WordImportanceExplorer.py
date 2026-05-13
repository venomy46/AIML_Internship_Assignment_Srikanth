from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "Machine learning is amazing and powerful",
    "Deep learning is a part of machine learning",
    "Artificial intelligence and machine learning are related",
    "Data science uses machine learning techniques",
    "Learning from data is important in AI"
]

# Apply TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Get feature names
words = vectorizer.get_feature_names_out()

# Convert to array
tfidf_array = X.toarray()

# Display top words for each document
for i, doc in enumerate(tfidf_array):
    print(f"\nDocument {i+1} Top Words:")
    sorted_indices = doc.argsort()[-3:]  # top 3 words
    for index in sorted_indices:
        print(words[index], ":", doc[index])