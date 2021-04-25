import pandas as pd
import nltk
import requests
from bs4 import BeautifulSoup
import re
import time

nltk.download('punkt')

##


df = pd.read_table("word.txt", header=None)

list_for_word = []
list_for_mean = []

for line in df.itertuples():
  morph = nltk.word_tokenize(line[1])
  search_url = 'https://ejje.weblio.jp/content/' + line[1]

  req = requests.get(search_url)
  time.sleep(5)

  soup = BeautifulSoup(req.text, "html.parser")
  get_word_mean = soup.find_all(class_='content-explanation ej')
  word_mean = ''

  for p in get_word_mean:
    word_mean += p.text

  if len(morph) > 1: 
    word_class = '［熟語］'
  else:
    get_word_class = soup.find_all(class_='KnenjSub')
    word_class = '［'

    for p in get_word_class:
      if p.text != '【語源】' and p.text !='英語による解説':
        word_class += p.text.strip() + ';'

    word_class = word_class[:-1] + '］'

  print(word_class, line[1], word_mean)
 
  list_for_word.append(word_class+line[1])
  list_for_mean.append(word_mean)

output_df = pd.DataFrame(list(zip(list_for_word, list_for_mean)))

output_df.to_csv("output_for_anki.txt", sep="\t", header=None, index=None)
