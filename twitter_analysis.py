import twint
import string
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob

# Configure twint
c = twint.Config()
c.Username = "noneprivacy"
c.Search = "great"
c.Limit = 10
c.Store_csv = False

# Run twint search
twint.run.Search(c)

# Retrieve tweets
tweets = twint.output.tweets_list

# Extract text from tweets
text_tweets = [tweet.tweet for tweet in tweets]

# Combine all text tweets into a single string
combined_text = ' '.join(text_tweets)

# Clean the text
lower_case = combined_text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenize the cleaned text
tokenized_words = cleaned_text.split()

# Define stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Filter out stop words
final_words = [word for word in tokenized_words if word not in stop_words]

# Perform sentiment analysis on keywords
sentiments = []
for word in final_words:
    blob = TextBlob(word)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)

# Count sentiment occurrences
sentiment_counts = Counter(sentiments)

# Prepare data for plotting
sentiment_values = sentiment_counts.keys()
sentiment_frequencies = sentiment_counts.values()

# Plot the sentiment analysis results
fig, ax = plt.subplots()
ax.bar(sentiment_values, sentiment_frequencies)
ax.set_xlabel('Sentiment')
ax.set_ylabel('Frequency')
ax.set_title('Twitter Sentiment Analysis')
plt.show()
