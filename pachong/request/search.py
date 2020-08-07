import requests
url='https://www.so.com/s'
try:
    kv={'q':'Python'}
    r = requests.get(url,params=kv)
    print(r.status_code,r.request.url,len(r.text))
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('false')