from bs4 import BeautifulSoup
markup='<p class="title"><b>The Little Prince</b></p>'
soup=BeautifulSoup(markup,"lxml")
print(soup.b)
print(type(soup.b))