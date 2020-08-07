import requests
url='https://www.amazon.cn/gp/product/B06XD783L2/ref=s9_acsd_al_bw_cr_x__a_w?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-12&pf_rd_r=GTWWRGS9CP5E087V1WR2&pf_rd_r=GTWWRGS9CP5E087V1WR2&pf_rd_t=101&pf_rd_p=c0f08bcd-fa79-4d17-9add-70791a14f65e&pf_rd_p=c0f08bcd-fa79-4d17-9add-70791a14f65e&pf_rd_i=116087071'

try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    print(r.status_code)
    r.encoding=r.apparent_encoding
#    print(r.headers)
    print(r.text[:1000])
except:
    print('false')