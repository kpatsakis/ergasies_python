from  p_tqdm import p_map
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
def get_data(url):
    headers = {"user-agent": ua.ie}
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    for d in soup.find_all("ul", {"class":"product-list"}):
        products=d.find_all("div", {"class":"product"})
        try:
            for p in products:
                titles=p.find_all("span", {"class":"product-title"})
                for t in titles:
                    title=t.text
                prices=p.find_all("div", {"class":"price"})
                for pr in prices:
                    tmp=pr.find_all("div", {"class":"price"})
                    for t in tmp:
                        price=t.text
                # print ("Product: %s Price: %s" %(title,price))
        except:
            pass
        # print ("done")

baseURL="https://www.plaisio.gr/pc-perifereiaka/laptops"
urls=[baseURL]
for i in range(1,64):
    tmp=baseURL+"/page-"+str(i+1)
    urls.append(tmp)

p_map(get_data,urls)
# for u in urls:
#     get_data(u)
