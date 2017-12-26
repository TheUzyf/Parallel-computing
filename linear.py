"""
	Вывести на экран названия дисциплин из зачетной книжки, 
	состоящих из двух и более слов.
"""

from pymorphy2 import MorphAnalyzer as MA 
from nltk.tokenize import WordPunctTokenizer as WPT  

ma = MA()
wt = WPT()

Subjects = {}
Result_sub = {}

try:
	file = open('subjects.txt', 'r',encoding='utf-8')
except FileNotFoundError:
	print("Файл не найден")
	raise SystemExit(1)

i=0	
for line in file:
	Subjects[i]=line
	i+=1

j=0
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
		Result_sub[key]=Subjects[key]
	j=0
	
		
for key in Result_sub:
	print(Result_sub[key])
	