from textblob import TextBlob
text = "I might buy it!"
blob = TextBlob(text)
print(blob.sentiment)
