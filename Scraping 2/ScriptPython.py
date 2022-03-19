# Mengimport Paackage
from selenium import webdriver
import urllib.request
import requests
import json
from datetime import datetime

# Mengambil konten web sebagai objek driver
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://kingchoice.me/the-100-most-beautiful-faces-in-kpop-2021/")

# Mengambil waktu sistem
time = datetime.now()
strTime = time.strftime("%d/%m/%Y %H:%M:%S")

# Membuat list kosong untuk menampung dictionary
# yang akan dieksport ke file json
ranklist = []

# Mengambil data ranking dan menambahkan ke list
a = int(0)
for data in driver.find_elements_by_class_name("rank-trend"):
    ranklist.append({"Rank" : data.text})

# Mengambil data gambar (link) dan menambahkan ke list
i = 1
a = int(0)
for img in driver.find_elements_by_class_name('option-image'):
    link = img.get_attribute('style')
    linkSplit = link.split('"')
    linkFix = "https://kingchoice.me" + linkSplit[1]
    print(linkFix)
    (ranklist[a]).update({"Pict" : linkFix})
    a = a + 1;
    r = requests.get(linkFix, stream=True, headers={'User-Agent': USER_AGENT})
    with open(str(i)+'.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    i = i +1

# Mengambil data nama dan kategori dan menambahkan ke list
a = int(0)
for data in driver.find_elements_by_class_name("flex-fill"):
    print(data.find_element_by_tag_name('a').text)
    (ranklist[a]).update({"Name" : data.find_element_by_tag_name('a').text})
    (ranklist[a]).update({"Kategori" : data.find_element_by_class_name('subtitle').text})
    a = a + 1

# Mengambil data vote dan menambahkan ke list bersamaan waktu sistem
a = int(0)
for data in driver.find_elements_by_class_name('vote-control'):
    print(data.find_element_by_class_name('up-votes').text)
    (ranklist[a]).update({"Votes" : data.find_element_by_class_name('up-votes').text})
    (ranklist[a]).update({"ScrapingTime" : strTime})
    a = a + 1;

print(ranklist)     # Menampilkan hasil list ranklist

# Memasukkan / mengeksport hasil list dictionary ke dalam json file
scraping = open("scrapingresult.json", "w")
json.dump(ranklist, scraping, indent = 6)
scraping.close()
    
driver.quit()

