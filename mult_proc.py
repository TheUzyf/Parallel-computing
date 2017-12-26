"""
	Вывести на экран названия дисциплин из зачетной книжки, 
	состоящих из двух и более слов.
"""
from multiprocessing import Process, freeze_support, Queue
from requests import get
from pymorphy2 import MorphAnalyzer as MA
from nltk.tokenize import WordPunctTokenizer as WPT

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
	
def search(q1,q2):
	Q=q2.get()
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
	q1.put(Result_sub)

N = 4

d = int(i/N)
e = d*N
n,m = 0,d

if e!=i:
	m+=1
	e+=1

t1 = [] 
t2 = [] 

for f in range(N):
	h1 = Queue()
	h2 = Queue()
	test=range(n,m)
	h2.put(test)
	t1+=[h1]
	t2+=[h2]
	if e!=i:
		n=m
		m+=d+1
		e+=1
	else:
		n=m
		m+=d

G =[]

if __name__ == '__main__':
	freeze_support()
	for f in range(N):
		g=Process(target=search, args= (t1[f],t2[f]))
		g.start()
		G+=[g]
	for pe in G:
		pe.join()
	
	Result_sub = t1[0].get()
	
	if N != 1:
		for t in t1[1:]:
			temp = {}
			temp = t.get()
			for (t) in temp:
				Result_sub[t]=temp[t]
				
	
	for key in Result_sub:
		print(Result_sub	[key])