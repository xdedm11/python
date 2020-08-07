def getText():
	txt=open('hamlet.txt','r').read()
	txt=txt.lower()
	for s in '|#$%&()*+-./;:<>=@[]\^_{}|~':
		txt=txt.replace(s,' ')
	return txt

hamlettxt=getText()
words=hamlettxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{:<10}{:>5}'.format(word,count))
