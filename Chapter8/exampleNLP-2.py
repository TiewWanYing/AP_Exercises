#! /usr/bin/env python3.9
#Natural Language Processing & Sentiment Analysis
# 1. pip install textblob
# Natural Language Dataset: 
# www.nltk.org/data.html
# https://gutenberg.org/ebook/
# https://gutenberg.org/cache/epub/1513/pg1513.txt

from textblob import TextBlob
from pathlib import Path

blob = TextBlob(Path('RomeoandJuliet.txt').read_text())
items = blob.word_counts.items()
print(items)
