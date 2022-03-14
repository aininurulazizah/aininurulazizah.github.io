# Import package requests dan beautifulsoup
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

# Request ke website
web = requests.get("https://republika.co.id/")

# Mengekstrak konten menjadi objek beautifulsoup
obj = BeautifulSoup(web.text, 'html.parser')

# Mengambil data waktu menjadi objek time
time = datetime.now()
strTime = time.strftime("%d/%m/%Y %H:%M:%S")
print(strTime)

# Menampilkan judul, kategori, waktu publish, waktu scrapping
print("Judul Berita")
print("============")
for judul in obj.find_all('div', class_='conten1'):
    print(judul.find('h1').text)
    print(judul.find('h2').text)
    print(judul.find('div', class_='date').text)
    print(time)
    print('\n')

# === Menyimpan Data ke Json ===
# Membuat list kosong
data = []

# Alokasi file json
f = open('D:\POLBAN\SEMESTER 2\Proyek 1\Pertemuan 7\Scrapping\Terkini.json', 'w')
for judul in obj.find_all('div', class_='conten1'):
    data.append({"Kategori" : judul.find('h1').text,
                 "Judul" : judul.find('h2').text,
                 "WaktuPublish" : judul.find('div', class_='date').text,
                 "WaktuScrapping" : strTime})

# Dump list dictionary menjadi json
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()
