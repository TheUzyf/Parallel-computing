"""
	Вывести на экран названия дисциплин из зачетной книжки, состоящих из двух и более слов.
"""

from bs4 import BeautifulSoup as BS
from pymorphy2 import MorphAnalyzer as MA
from nltk.tokenize import WordPunctTokenizer as WPT  
from requests import get  

ma = MA()
wt = WPT()

Subjects = {}
Result_sub = {}

try:
	file = open('subjects.txt', 'r',encoding='utf-8')
except FileNotFoundError:
	print("Файл не найден")
	raise SystemExit(1)

i=1	
for line in file:
	Subjects[i]=line
	i+=1

j=0
k=1
for key in Subjects:
	for word in wt.tokenize(Subjects[key]):
		for p in ma.parse(word):
			if ("NOUN") in p.tag:
				j+=1
				break
			if ("ADJF") in p.tag:
				j+=1
				break
			if ("ADJS") in p.tag:
				j+=1
				break
			if ("PRTF") in p.tag:
				j+=1
				break
			if ("PRTS") in p.tag:
				j+=1
				break
	if j>1:
		Result_sub[k]=Subjects[key]
		k+=1
	j=0
	
		
for key in Result_sub:
	print(Result_sub[key])
	