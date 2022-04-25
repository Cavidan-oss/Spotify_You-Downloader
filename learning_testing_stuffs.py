import urllib.request
import re
from bs4 import BeautifulSoup
import requests


url = 'https://www.youtube.com/results?search_query=Madrigal+-+Seni+Dert+Etmeler+%28Official+Audio%29'
# html = urllib.request.urlopen(url)
# new_html = html.read().decode()

# video_ids = re.findall(r"watch\?v=(\S{11})", new_html) 

musics_name = 'Reckol&cakal - Benimle Gel'

query = "+".join(musics_name.split(' ')).encode(encoding = 'UTF-8', errors = 'strict')
search_query = f"https://www.youtube.com/results?search_query={query}"




response = requests.get(url)

content = response.content

soup = BeautifulSoup(response.text, 'html.parser')

new_ids = re.findall(r"watch\?v=(\S{11})", str(soup))






# https://www.youtube.com/results?search_query=Reckol%26cakal+-+Benimle+Gel

# "https://www.youtube.com/results?search_query=b'Reckol&cakal+-+Benimle+Gel'"








################################################### Worked One ##############3

from urllib.parse import urlencode


musics_name = 'cakal - ANTRIKOT'

w_query = "".join(musics_name.split(' ')).encode(encoding = 'UTF-8', errors = 'strict')
base = f"https://www.youtube.com/results"
search_q = f"{base}?{urlencode({'search_query':w_query})}"





response = requests.get(search_q)

content = response.content

worked_soup = BeautifulSoup(response.text, 'html.parser')

worked_new_ids = re.findall(r"watch\?v=(\S{11})", str(worked_soup))







#################################################

musics_name = 'Reckol&cakal - Benimle Gel'

w_query = "".join(musics_name.split(' ')).encode(encoding = 'UTF-8', errors = 'strict')
base = f"https://www.youtube.com/results"
search_q = f"{base}?{urlencode({'search_query':w_query})}"





response = requests.get(search_q)

content = response.content

worked_soup = BeautifulSoup(response.text, 'html.parser')

worked_new_ids = re.findall(r"watch\?v=(\S{11})", str(worked_soup))






dat = """akal - İmdat Downloaded_name cakal - İmdat (Official Audio) |Sucess
UZI - ARASAN DA Downloaded_name UZI - ARASAN DA |Sucess
Semicenk&Funda Arar - Al Sevgilim Downloaded_name Semicenk & Funda Arar - Al Sevgilim |Sucess
Lvbel C5 - GELMEZSEN GELME Downloaded_name LVBEL C5 - GELMEZSEN GELME |Sucess
Canbay & Wolker - Leylim Yar Downloaded_name Canbay & Wolker - Leylim Yar (Official Video) |Sucess
UZI - PAPARAZZI Downloaded_name UZI - PAPARAZZI |Sucess
Can Koç - Gökyüzünü Tutamam Downloaded_name Can Koç - Gökyüzünü Tutamam (Official Lyric Video) |Sucess
Kalben - Yara Downloaded_name Kalben - Yara |Sucess
Sefo&Revart - yarım kalır Downloaded_name Sefo, @Revart  - yarım kalır (prod.by Aerro) |Sucess
Heijan&Muti - Birader Downloaded_name Heijan feat. Muti - Birader (Official Video) |Sucess
Reckol&BEGE - Feragât Downloaded_name Reckol X BEGE - Feragât (Official Music Video) |Sucess
Gökhan Türkmen - Mahşer Downloaded_name Mahşer [Official Video] - Gökhan Türkmen #Mahşer |Sucess
Sefo - Affettim Downloaded_name Sefo - Affettim (prod.by Aerro) |Sucess
Reckol&cakal - Benimle Gel Downloaded_name Reckol & Cakal - Benimle Gel (Official Music Video) |Sucess
Lvbel C5&Batuflex - GÖNDER GELSİN Downloaded_name LVBEL C5 X BATUFLEX - GÖNDER GELSİN |Sucess
Diyar Pala - Anla Downloaded_name Diyar Pala - Anla |Sucess
Madrigal - Seni Dert Etmeler Downloaded_name Madrigal - Seni Dert Etmeler (Official Audio) |Sucess
GOKO! - EVA & MIA Downloaded_name GOKO! - EVA&MIA (Official Video) |Sucess
UZI - CINDY Downloaded_name UZI - CINDY (Official Video) |Sucess
Montiego&Lvbel C5 - Yallah Downloaded_name Montiego & Lvbel C5 & Batuflex - Yallah |Sucess
cakal&Mavi - Gözler Downloaded_name Cakal x Mavi - Gözler Lyrics Sözleri |Sucess
No.1&Melek Mosso - Yarım Kalan Sigara Downloaded_name 13. No.1 - Yarım Kalan Sigara feat. Melek Mosso #Kron1k |Sucess
UZI - Umrumda Değil Downloaded_name Uzi - Umrumda Değil (Official Video) |Sucess
cakal - Lütfen Downloaded_name CAKAL - LÜTFEN (Official Music Video) |Sucess
Lvbel C5 - 10 NUMARA Downloaded_name LVBEL C5 - '10 numara, |Sucess
Rei 6 - Ah Canım Sevgilim - Demo Downloaded_name Rei - Ah Canım Sevgilim |Sucess
cakal - Riv Riv Riv Downloaded_name Riv Riv Riv |Sucess
Harry Styles - As It Was Downloaded_name Harry Styles - As It Was (Official Video) |Sucess
Ayaz Erdoğan - Hep Mi Ben Downloaded_name Ayaz Erdoğan - Hep Mi Ben? |Sucess
Dolu Kadehi Ters Tut&Sedef Sebüktekin - Gitme Downloaded_name Dolu Kadehi Ters Tut & Sedef Sebüktekin - Gitme (Zorlu PSM %100 Studio Canlı Performans) |Sucess
Semicenk - Düşer Aklıma Downloaded_name Semicenk - Düşer Aklıma |Sucess
KÖFN - Bi' Tek Ben Anlarım Downloaded_name KÖFN - Bi' Tek Ben Anlarım - (Official Video) |Sucess
cakal - Mahvettim Downloaded_name Cakal - Mahvettim (Official Music Video) |Sucess
Dolu Kadehi Ters Tut - Hiç İyi Değilim Downloaded_name Dolu Kadehi Ters Tut - Hiç İyi Değilim (Official Audio) |Sucess
Motive - KÂR Downloaded_name KÂR |Sucess
Bartofso&Murda - RS Downloaded_name Bartofso X Murda X UZI - RS - lyrics - şarkı sözleri |Sucess
Berk Baysal - Yaralarını Ben Sarayım Downloaded_name Berk Baysal - Yaralarını Ben Sarayım ( Official Audio ) |Sucess
Elley Duhé - MIDDLE OF THE NIGHT Downloaded_name Elley Duhé - Middle of the Night (Lyrics) |Sucess
Yüksek Sadakat - Kafile Downloaded_name Yüksek Sadakat - Kafile |Sucess
Kahraman Deniz - Son Durağın Downloaded_name Kahraman Deniz - Son Durağın (Official Audio) |Sucess
Evdeki Saat - Uzunlar - V1 Downloaded_name Evdeki Saat - Uzunlar V1 (Official Video) |Sucess
EDIS - Arıyorum Downloaded_name Edis - Arıyorum (Official Video) |Sucess
cakal - ANTRIKOT Downloaded_name Cakal - Antrikot (Official Music Video) |Sucess
Tom Odell - Another Love Downloaded_name Tom Odell - Another Love (Official Video) |Sucess
Güneş - Suçlarımdan Biri Downloaded_name Güneş - Suçlarımdan Biri (Official Video) |Sucess
Lvbel C5&Batuflex - ralli Downloaded_name LVBEL C5 X BATUFLEX - ralli 'babe, |Sucess
Sefo - Bilmem Mi? Downloaded_name Sefo - Bilmem Mi? (prod.by Aerro) |Sucess
Sefo&Reynmen - Bonita Downloaded_name Sefo & Reynmen - Bonita (prod. by Aerro) |Sucess
Derya Uluğ - Sana Çıkıyor Yollar - Kaderimin Oyunu Orijinal Dizi Müziği Downloaded_name Derya Uluğ - Sana Çıkıyor Yollar (Kaderimin Oyunu Orijinal Jenerik Dizi Müziği) |Sucess
"""


print(len(dat.split('\n')))




with open('data.txt.txt', 'r') as file:
    data = file.read()
    

print(data.rfind('Download Error'))


print(data[data.rfind('Download Error')-1000: data.rfind('Download Error')+1000])
















