import requests
url='https://item.jd.com/26396385665.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('false')