import basis
import re

if __name__ == '__main__':
    for tag in basis.soup.find_all(re.compile('b')):
        print(tag.name)
    #print(basis.soup.find_all(id=re.compile('link')))
    print(basis.soup.find_all(string=re.compile('python')))