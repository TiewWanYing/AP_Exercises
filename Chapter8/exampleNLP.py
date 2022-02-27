#Natural Language Processing & Sentiment Analysis

#1. pip install textblob
#Natural language Dataset:
# www.nltk.org/data.html
# https://gutenberg.org/ebook/
# https://gutenberg.org/cache/epub/1513/pg1513.txt

from textblob import TextBlob
text = 'Tomorrow will be a great weekend for us'
blob = TextBlob(text)
blob.detect_language()
chinese = blob.translate(to='zh')
spanish = blob.translate(to='es')
spanish.detect_language()	#'es'

# Polarity: -1.0 (Negative) to 1.0 (Positive)
# Subjectivity: 0.0 (Objective) to 1.0 (Subjective)
blob.sentiment

text1='Yesterday was a beautiful day, but today looks like bad weather'
blob1= TextBlob(text1)
blob1.sentiment

blob = TextBlob (Path('RomeoAndJuliet.txt').read_text())
items = blob.word_counts.items()
