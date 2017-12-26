"""
	Вывести на экран названия дисциплин из зачетной книжки, 
	состоящих из двух и более слов.
"""

from queue import Queue, Empty
from tkinter import *
from pymorphy2 import MorphAnalyzer as MA  
from nltk.tokenize import WordPunctTokenizer as WPT 
from requests import get

root = Tk()
ma = MA()
wt = WPT()

try:
	file = open('subjects.txt', 'r',encoding='utf-8')
except FileNotFoundError:
	print("Файл не найден")
	raise SystemExit(1)

Subjects = {}
Result_sub = {}	
	
i=0	
for line in file:
	Subjects[i]=line
	i+=1

q = Queue()
	
def search():
	Q=q.get()
	j=0
	for kq in Q:
		qSubjects = Subjects[kq]
		for word in wt.tokenize(qSubjects):
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
			Result_sub[kq]=Subjects[kq]
		j=0

N = 4
d = int(i/N)
e = int(i%N)
n,m = 0,d
	
for f in range(N+1):
	test=range(n,m)
	q.put(test)
	root.after(1,search)
	n+=d
	if f == N-1:
		m+=e
	else:
		m+=d

root.mainloop()	
	
for key in Result_sub:
	print(Result_sub[key])
	