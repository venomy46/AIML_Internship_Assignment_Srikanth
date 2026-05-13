# Sample text
text = input("Enter a sentence: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
punctuation = ".,!?;:'\"()-"
clean_text = ""
for char in text:
    if char not in punctuation:
        clean_text += char

# Remove stopwords
stopwords = ["is", "the", "and", "a", "an", "in", "on", "at", "to", "for", "of"]

words = clean_text.split()
filtered_words = []

for word in words:
    if word not in stopwords:
        filtered_words.append(word)

# Final cleaned text
result = " ".join(filtered_words)

print("Cleaned Text:", result)