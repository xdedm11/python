import re
match=re.search(r'[1-9]\d{5}','abdj sjf134543dj420486')
if match:
    print(match.group(0),type(match))
print(match.string,match.re,match.pos,match.endpos)
print(match.start(),match.end(),match.span())
match=re.match(r'[1-9]\d{5}','356777')
if match:
    print(match.group(0))

ls=re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
print(ls)

print(re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1))

for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0))

print(re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084'))

#贪婪
m=re.search(r'py.*n','pyanbncndn')
print(m.group(0))
#最小匹配
m=re.search(r'py.*?n','pyanbncndn')
print(m.group(0))