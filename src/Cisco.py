import requests
from bs4 import BeautifulSoup

#URL ye gider kullanıcıdan aldığı path adresindeki ürünün sayfasındaki html kodunu parsaller.
def pullData():
    url_address = "https://www.cisco.com/c/en/us/products/collateral"
    path_address = input("enter patch address: ")
    response = requests.get(f"{url_address}{path_address}")#path adresini dinamik olarak almak için.
    soup = BeautifulSoup(response.text, 'html.parser')

    getFinalData(soup)

#Alınan içeriğin doğru ve tüm uzantılar için geçerli olan tag yolunu parsaller.
def getFinalData(soup):
    main_content = soup.find("div", class_ = ["col wide document", "WordSection1"])
    first_layer = main_content.find("tbody")
    final_content = first_layer.find_all("td")

    convertFinalSituation(final_content)

#Veriyi kullanıcıların okuyacağı formata çevirir.
def convertFinalSituation(content):
    list_content = [i.text for i in content]
    print(list_content[2])

#Test Edilen Sayfalar;
#https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-4500-series-switches/eos-eol-notice-c51-744420.html
#https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/isr4461-series-platform-eol.html
pullData()