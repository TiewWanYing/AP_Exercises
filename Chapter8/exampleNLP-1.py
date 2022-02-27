#! /usr/bin/env python3.9
#Natural Language Processing & Sentiment Analysis
# 1. pip install textblob
# Natural Language Dataset: 
# www.nltk.org/data.html
# https://gutenberg.org/ebook/
# https://gutenberg.org/cache/epub/1513/pg1513.txt

from textblob import TextBlob
from pathlib import Path

text1 = 'Tomorrow will be a great weekend for us'
blob1 = TextBlob(text1)
blob1.detect_language()
print(blob1.translate(to='ja'))

# Polarity: -1.0 (Negative) to 1.0 (Positive)
# Subjectivity : 0.0 (Objective) to 1.0 (Subjective) 
print(blob1.sentiment)

text2 = 'Yesterday was a beautiful day, but today looks like bad weather'
blob2 = TextBlob(text2)
blob2.sentiment
a= blob2.sentiment.polarity
print(blob2.translate(to='ms'))
print(blob2.translate(to='es'))
print ("{0:.2f}".format(a))




