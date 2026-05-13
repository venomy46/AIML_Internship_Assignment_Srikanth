# Simple word-based sentiment analyzer

positive_words = ["good", "great", "amazing", "excellent", "love", "awesome"]
negative_words = ["bad", "worst", "boring", "poor", "hate", "terrible"]

def analyze_sentiment(review):
    review = review.lower()
    words = review.split()
    
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Test on 5 reviews
reviews = [
    "The movie was amazing and awesome",
    "It was the worst film I have seen",
    "The story was good but a bit boring",
    "I love the acting, excellent work",
    "It was okay not great not bad"
]

for r in reviews:
    print("Review:", r)
    print("Sentiment:", analyze_sentiment(r))
    print()