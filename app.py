import streamlit as st
import numpy as np
import pandas as pd
import string
import random
import Levenshtein
import re
import nltk
import os
# Atur zona waktu menjadi Asia/Jakarta
os.environ['TZ'] = 'Asia/Jakarta'
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from datetime import datetime 
import pytz
import locale
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')



# # URL gambar background di repositori GitHub
# background_image_url = "https://raw.githubusercontent.com/YosefAlfredo15/darmabot/main/"  # Ganti dengan URL gambar Anda

# # Menambahkan gambar sebagai background dengan lebar 100%
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url('{background_image_url}');
#         background-size: cover;  /* Untuk menutupi seluruh area background */
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# with open("D:/TUGAS AKHIR/desain.html", "r") as file:
#     html_code = file.read()

# print(html_code)

import streamlit as st

# Judul di tengah dengan HTML
# Path gambar
# Path gambar
image_path = "chatbot.webp"  # Ganti dengan path gambar Anda

# Menambahkan gambar di halaman utama
st.image(image_path, width=100)

# Menambahkan judul di halaman utama
st.markdown("<h1 style='text-align: center;'>SI Darma Chatbot</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Halo! nama aku darma bot, Silahkan Ajukan Pertanyaan Anda!</p>", unsafe_allow_html=True)



#pertanyaan dan jawaban
responses = {

    "pagi": [
        "<h1>Selamat Pagi, Ada yang bisa saya bantu?</h1>",
        "<h1>Selamat Pagi, Ada yang perlu dibicarakan?</h1>",
        "<h1>Selamat Pagi, Bagaimana saya bisa membantu Anda hari ini?</h1>",
        "<h1>Selamat Pagi, Apa kabar?</h1>",
        "<h1>Selamat Pagi juga! Ada yang bisa saya bantu?</h1>",
        "<h1>Halo! Selamat Pagi. Ada yang perlu dibicarakan?</h1>",
    ],
# Selamat Pagi (salam)
    "pagi" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi kawan" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi teman" : ["Selamat Pagi , Ada yang bisa saya bantu?"],

# Selamat Siang (salam)
    "siang" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang kawan" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang teman" : ["Selamat Siang , Ada yang bisa saya bantu?"],

# Selamat Sore (salam)
    "sore" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore kawan" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore teman" : ["Selamat Sore , Ada yang bisa saya bantu?" ],

# Selamat Malam (salam)
    "malam" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam kawan" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam teman" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam" : ["Selamat Malam , Ada yang bisa saya bantu?"],

# Hai (sapaan)
    "hai" : ["Hai😄, ada yang bisa saya bantu?"],
    "halo" :["Halo😄, ada yang bisa saya bantu?"],
    "hallo" :["Halo😄, ada yang bisa saya bantu?"],
    "hi" : ["Hi😄, ada yang bisa saya bantu?"],
    "hay" : ["Hay😄, ada yang bisa saya bantu?"],
    "hy" : ["Hy😄, ada yang bisa saya bantu?"],


# salam bot (salam)
    "hai darma bot "  : ["Hai😄, ada yang bisa saya bantu?"],
    "halo darma bot" :["Halo😄, ada yang bisa saya bantu?"],
    "hallo darma bot" :["Halo😄, ada yang bisa saya bantu?"],
    "hi darma bot" : ["Hi😄, ada yang bisa saya bantu?"],
    "hay darma bot" : ["Hay😄, ada yang bisa saya bantu?"],
    "hy darma bot" : ["Hy😄, ada yang bisa saya bantu?"],


# salam bot (salam)
    "hai bot" : ["Hai😄, ada yang bisa saya bantu?"],
    "hai chatbot" : ["Hai😄, ada yang bisa saya bantu?"],
    
    "halo bot" :["Halo😄, ada yang bisa saya bantu?"],
    "halo chatbot" :["Halo😄, ada yang bisa saya bantu?"],
    
    "hallo bot" :["Halo😄, ada yang bisa saya bantu?"],
    "hallo chatbot" :["Halo😄, ada yang bisa saya bantu?"],
    
    "hi bot" : ["Hi😄, ada yang bisa saya bantu?"],
    "hi chatbot" : ["Hi😄, ada yang bisa saya bantu?"],
    
    "hay bot" : ["Hay😄, ada yang bisa saya bantu?"],
    "hay chatbotbot" : ["Hay😄, ada yang bisa saya bantu?"],
    
    "hy bot" : ["Hy😄, ada yang bisa saya bantu?"],
    "hy chatbotbot" : ["Hy😄, ada yang bisa saya bantu?"],
    

    "hai kawan" : ["Hai😄, ada yang bisa saya bantu?"],
    "halo kawan " :["Halo😄, ada yang bisa saya bantu?"],
    "hallo kawan " :["Halo😄, ada yang bisa saya bantu?"],
    "hi kawan " : ["Hi😄, ada yang bisa saya bantu?"],
    "hay kawan " : ["Hay😄, ada yang bisa saya bantu?"],
    "hy kawan " : ["Hy😄, ada yang bisa saya bantu?"],

    "hai teman" : ["Hai😄, ada yang bisa saya bantu?"],
    "halo teman" :["Halo😄, ada yang bisa saya bantu?"],
    "hallo teman" :["Halo😄, ada yang bisa saya bantu?"],
    "hi teman" : ["Hi😄, ada yang bisa saya bantu?"],
    "hay teman" : ["Hay😄, ada yang bisa saya bantu?"],
    "hy teman" : ["Hy😄, ada yang bisa saya bantu?"],

    "hai bot" : ["Hai😄, ada yang bisa saya bantu?"],
    "halo bot" :["Halo😄, ada yang bisa saya bantu?"],
    "hallo bot" :["Halo😄, ada yang bisa saya bantu?"],
    "hi bot" : ["Hi😄, ada yang bisa saya bantu?"],
    "hay bot" : ["Hay😄, ada yang bisa saya bantu?"],
    "hy bot" : ["Hy😄, ada yang bisa saya bantu?"],

    "salam": ["Salam juga!", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "kenal" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "salam kenal ya" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "salam kenal" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],

    "sip": ["Salam juga!", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "iya" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "oke" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "okeh" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    
#Perasaan
    "baik" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "sehat" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Alhamdullilah, sehat": ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Alhamdullilah, baik": ["Syukurlah jika baik, Ada yang bisa saya bantu? "],
    "Puji tuhan, baik" : ["Syukurlah jika baik, Ada yang bisa saya bantu? "],
    "Puji tuhan, sehat" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "baik baik saja" : ["Syukurlah jika baik, Ada yang bisa saya bantu? "],
    "sehat sehat saja" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "good" : ["Good, Ada yang bisa saya bantu? "],
    "sedih" : ["Sudahi kesedihan mu ya😄, ada yang bisa saya bantu"],
    "Tidak Sehat" :["Semoga lekas sembuh, perbanyak istirahat. Ada yang bisa saya bantu?"],
    "kurang enak badan" : ["Semoga lekas sembuh, perbanyak istirahat. Ada yang bisa saya bantu?"],
    "aku kecewa" : ["Ada apa?, Ada yang bisa saya bantu?"],
    "aku tidak senang" : ["Mengapa, Ada yang bisa saya bantu?"],

    "kabar" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "apa kabar" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "bagaiamana kabar mu" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "bagaiamana kabar kamu" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "kamu apa kabar" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu?"],
    "kalo kamu" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "kamu sendiri apa kabar" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu? "],
    "Kamu sehat?" : ["Aku selalu sehat dong, Ada yang bisa saya bantu? "],
    "kamu kabarnya gimana" : ["Saya adalah asisten virtual, jadi saya tidak memiliki perasaan fisik seperti manusia. Namun, saya selalu siap dan senang membantu Anda dengan pertanyaan atau masalah apa pun yang Anda miliki. Apakah ada yang dapat saya bantu?"],


    "kamu lagi apa" :["Sedang mengaggur nih, Ada yang bisa saya bantu?"],
    "kamu sedang apa" :["Sedang mengaggur nih, Ada yang bisa saya bantu?"],
    "sedang apa" :["Sedang mengaggur nih, Ada yang bisa saya bantu?"],
    "lagi apa" :["Sedang mengaggur nih, Ada yang bisa saya bantu?"],
    "apa" : ["Apa yang ingin kamu tanyakan?"],
    "Siapa" : ["Siapa?. Maksud kamu siapa aku? (Aku adalah Darma Bot)"],
    "Bagaimana" : ["Bagaimana?. Coba jelaskan kembali, apa yang kamu tanyakan?"],
    "mengapa" :["Mengapa?. Coba jelaskan kembali, apa yang mau kamu tanyakan?"],

    "terimakasih" : ["Baik, sama-sama"],
    "terimakasih darma bot" : ["Baik, sama-sama"],
    "trims" : ["Baik, sama-sama"],
    "trims ya" : ["Baik, sama-sama"],
    "makasih" : ["Baik, sama-sama"],
    "makasih darma bot" : ["Baik, sama-sama"],
    "terimakasih ya" : ["Baik, sama-sama"],
    "terimakasih ya darma bot" : ["Baik, sama-sama"],
    "makasih ya" : ["Baik, sama-sama"],
    "makasih ya darma bot" : ["Baik, sama-sama"],
    "thankyou" :  ["Urwellcome"],
    "thankyou darma bot" :  ["Urwellcome"],
    "thankyou ya" : ["Urwellcome"],
    "thanks" : ["Urwellcome"],
    "thanks ya" : ["Urwellcome"],
    
    "baiklah kalo begitu terimakasih ya" : ["Baik, sama-sama"],
    "baiklah jika begitu terimakasih ya" : ["Baik, sama-sama"],
    "baiklah terimakasih ya" : ["Baik, sama-sama"],
    "okelah kalo begitu terimakasih ya" : ["Baik, sama-sama"],
    "okelah terimakasih ya" : ["Baik, sama-sama"],
    "oke terimakasih ya" : ["Baik, sama-sama"],
    "oke kalau begitu terimakasih ya" : ["Baik, sama-sama"],
    "oke jika begitu terimakasih ya" : ["Baik, sama-sama"],
    
    
    "baiklah kalo begitu terimakasih ya darma bot" : ["Baik, sama-sama"],
    "baiklah jika begitu terimakasih ya darma bot" : ["Baik, sama-sama"],
    "baiklah terimakasih ya darma bot" : ["Baik, sama-sama"],
    "okelah kalo begitu terimakasih ya darma bot" : ["Baik, sama-sama"],
    "okelah terimakasih ya darma bot" : ["Baik, sama-sama"],
    "oke terimakasih ya darma bot" : ["Baik, sama-sama"],
    "oke kalau begitu terimakasih ya darma bot" : ["Baik, sama-sama"],
    "oke jika begitu terimakasih ya darma bot" : ["Baik, sama-sama"],
    
    
    "baiklah kalo begitu makasih ya" : ["Baik, sama-sama"],
    "baiklah jika begitu makasih ya" : ["Baik, sama-sama"],
    "baiklah makasih ya" : ["Baik, sama-sama"],
    "okelah kalo begitu makasih ya" : ["Baik, sama-sama"],
    "okelah makasih ya" : ["Baik, sama-sama"],
    "oke makasih ya" : ["Baik, sama-sama"],
    "oke kalau begitu makasih ya" : ["Baik, sama-sama"],
    "oke jika begitu makasih ya" : ["Baik, sama-sama"],
    
    "baiklah kalo begitu makasih ya darma bot" : ["Baik, sama-sama"],
    "baiklah jika begitu makasih ya darma bot" : ["Baik, sama-sama"],
    "baiklah makasih ya darma bot" : ["Baik, sama-sama"],
    "okelah kalo begitu makasih ya darma bot" : ["Baik, sama-sama"],
    "okelah makasih ya darma bot" : ["Baik, sama-sama"],
    "oke makasih ya darma bot" : ["Baik, sama-sama"],
    "oke kalo begitu makasih ya darma bot" : ["Baik, sama-sama"],
    "oke jika begitu makasih ya darma bot" : ["Baik, sama-sama"],
    
    "baiklah kalo begitu trims ya" : ["Baik, sama-sama"],
    "baiklah jika begitu trims ya" : ["Baik, sama-sama"],
    "baiklah trims ya" : ["Baik, sama-sama"],
    "okelah kalo begitu trims ya" : ["Baik, sama-sama"],
    "okelah trims ya" : ["Baik, sama-sama"],
    "oke trims ya" : ["Baik, sama-sama"],
    "oke kalo begitu trims ya" : ["Baik, sama-sama"],
    "oke jika begitu trims ya" : ["Baik, sama-sama"],
    
    "baiklah kalo begitu trims ya darma bot" : ["Baik, sama-sama"],
    "baiklah jika begitu trims ya darma bot" : ["Baik, sama-sama"],
    "baiklah trims ya darma bot" : ["Baik, sama-sama"],
    "okelah kalo begitu trims ya darma bot" : ["Baik, sama-sama"],
    "okelah trims ya darma bot" : ["Baik, sama-sama"],
    "oke trims ya darma bot" : ["Baik, sama-sama"],
    "oke kalo begitu trims ya darma bot" : ["Baik, sama-sama"],
    "oke jika begitu trims ya darma bot" : ["Baik, sama-sama"],

    "baiklah kalo begitu thanks ya" : ["Baik, sama-sama"],
    "baiklah jika begitu thanks ya" : ["Baik, sama-sama"],
    "baiklah thanks ya" : ["Baik, sama-sama"],
    "okelah kalo begitu thanks ya" : ["Baik, sama-sama"],
    "okelah thanks ya" : ["Baik, sama-sama"],
    "oke thanks ya" : ["Baik, sama-sama"],
    "oke kalo begitu thanks ya" : ["Baik, sama-sama"],
    "oke jika begitu thanks ya" : ["Baik, sama-sama"],
    
    
    "baiklah kalo begitu thanks ya darma bot" : ["Baik, sama-sama"],
    "baiklah jika begitu thanks ya darma bot" : ["Baik, sama-sama"],
    "baiklah thanks ya darma bot" : ["Baik, sama-sama"],
    "okelah kalo begitu ya darma bot" : ["Baik, sama-sama"],
    "okelah thanks ya darma bot" : ["Baik, sama-sama"],
    "oke thanks ya darma bot" : ["Baik, sama-sama"],
    "oke kalo begitu ya darma bot" : ["Baik, sama-sama"],
    "oke jika begitu ya darma bot" : ["Baik, sama-sama"],
    

    "baiklah kalo begitu" : ["Baik, ada lagi yang ingin anda tanyakan?"],
    "baiklah jika begitu" : ["Baik, ada lagi yang ingin anda tanyakan?"],
    "okelah kalo begitu" : ["Baik, ada lagi yang ingin anda tanyakan?"],
    "okelah jika begitu" : ["Baik, ada lagi yang ingin anda tanyakan?"],





    "bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "bertanya dong" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "bertanya boleh" :["Silahkan","Apa yang anda ingin tanyakan?"],
    
    "saya ingin bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya ingin bertanya dong" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya ingin bertanya boleh" :["Silahkan","Apa yang anda ingin tanyakan?"],
    
    "saya mau bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya mau bertanya dong" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya mau bertanya boleh" :["Silahkan","Apa yang anda ingin tanyakan?"],
    
    "mau tanya tanya" :["Silahkan, apa yang ingin anda tanyakan?"],
    "mau tanya tanya dong" :["Silahkan, apa yang ingin anda tanyakan?"],
    "mau tanya tanya boleh" :["Silahkan, apa yang ingin anda tanyakan?"],
    
    "saya mau tanya tanya" :["Silahkan, apa yang ingin anda tanyakan?"],
    "saya mau tanya tanya dong" :["Silahkan, apa yang ingin anda tanyakan?"],
    "saya mau tanya tanya boleh" :["Silahkan, apa yang ingin anda tanyakan?"],
    
    "saya mau tanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya mau tanya dong" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya mau tanya boleh" :["Silahkan","Apa yang anda ingin tanyakan?"],
    
    

    
    
    "pengumuman ukdc" :  ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"], 
    "informasi ukdc" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"], 
    "info ukdc" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],
    "saya mau tau info" : ["Silahkan, Informasi apa yang anda ingin tanyakan?"],
    "mau mau tau info tentang ukd" : ["Silahkan, Informasi apa yang anda ingin tanyakan?"],
    "saya mau tau" : ["Silahkan","Apa yang anda ingin ketahui?"],
    "mau tau tentang info ukdc dong" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],
    "saya mau tau tentang info ukdc dong" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],    
    "saya mau tau tentang informasi ukdc dong" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],
    "saya mau tau tentang informasi kampus ukdc dong" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],
    "saya mau tau tentang info kampus ukdc dong" : ["Silahkan, Jika anda ingin mengetahui informasi dan pengumuman tentang UKDC silahkan klik link ini https://siakad.ukdc.ac.id/spmbfront/pengumuman"],
    
    "siapa kamu"  : ["Halo, Saya adalah Darma Bot"],
    "nama kamu siapa"  : [" Halo, Saya adalah Darma Bot"],
    "siapa nama kamu"  : [" Halo, Saya adalah Darma Bot"],
    "kamu siapa" :  ["Halo, Saya adalah Darma Bot"],
    "kamu itu siapa" :  [" Halo, Saya adalah Darma Bot"],
    "siapa kamu itu" :  ["Halo, Saya adalah Darma Bot"],
    "nama": ["Saya adalah Darma Bot.", "Anda bisa memanggil saya Darma.", "Salam kenal!"],

    "apa itu ukdc" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor."],
    "apa ukdc itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa itu kampus UKDC" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa kampus UKDC itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa Univeristas UKDC itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa itu Univeristas UKDC" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa Univeristas Katolik Darma Cendika itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa itu Univeristas Katolik Darma Cendika" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "UKDC itu kampus apa" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "Kampus UKDC itu apa" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "Univ Darma cendika itu apa" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "Kampus Darma Cendika itu apa" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "Universitas UKDC itu apa" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "Univeristas Katolik Darma Cendika itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa kampus UKDC itu" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa yang kamu ketahui tentang UKDC?" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa yang kamu ketahui tentang kampus UKDC?" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa yang kamu ketahui tentang darma cendika surabaya?" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "apa yang kamu ketahui tentang kampus darma cendika UKDC?" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "UKDC itu apa sih" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "coba jelaskan mengenai kampus ukdc" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],
    "tolong jelaskan apa itu kampus ukdc" :["Universitas Katolik Darma Cendika (UKDC) merupakan salah satu Universitas Katolik yang berkembang pesat di Indonesia. Kami berusaha untuk memberikan pendidikan tinggi yang berkualitas bagi siswa baik secara akademis dan karakter. Berkomitmen untuk menjalankan visi dan misinya menjadi universitas yang unggul dalam memberikan pendidikan karakterpreneurship di Indonesia. Dalam upaya menghadapi perkembangan lingkungan kerja modern, UKDC secara aktif menjalin kerjasama dengan berbagai institusi baik di dalam maupun di luar negeri. Kerjasama ini diharapkan dapat menghasilkan saling menguntungkan dan mampu meningkatkan kualitas pembelajaran yang diperoleh mahasiswa. Dengan terus meningkatkan kualitas tenaga pengajar, fasilitas kampus dan juga tata kelola pendidikan tinggi, Universitas Katolik Darma Cendika akan selalu berperan aktif dalam menghasilkan lulusan yang berkualitas sehingga mampu memberikan kontribusi bagi pembangunan nasional di berbagai sektor"],

    "jurusan ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan apa saja yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi apa saja yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan apa yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan apa aja yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],

    "apa visi kampus ukdc" :["Visi : “Menjadi Universitas yang unggul dalam mengembangkan characterpreneurship di Indonesia."],
    "apa visi kampus darma cendika" : ["Visi = “Menjadi Universitas yang unggul dalam mengembangkan characterpreneurship di Indonesia."],
    "apa misi kampus darma cendika" : ["Misi = Menyelenggarakan pendidikan tinggi yang integratif guna menghasilkan lulusan yang berkarakter wirausaha yang jujur, peduli dan bertanggung jawab. b. Menciptakan ekosistem pendidikan yang kolaboratif dan kondusif untuk mengembangkan budaya inovasi. c. Mewujudkan kualitas dosen dan tenaga kependidikan yang unggul berdasarkan nilai-nilai kebenaran dan kasih sayang. d. Mengoptimalkan civitas akademika dan pemangku kepentingan dalam melaksanakan tata kelola perguruan tinggi yang kredibel, transparan, akuntabel, bertanggung jawab, dan berkeadilan secara berkelanjutan. e. Membangun kemitraan dalam rangka meningkatkan kesejahteraan masyarakat."],
    "apa misi kampus darma cendika" : ["Misi = Menyelenggarakan pendidikan tinggi yang integratif guna menghasilkan lulusan yang berkarakter wirausaha yang jujur, peduli dan bertanggung jawab. b. Menciptakan ekosistem pendidikan yang kolaboratif dan kondusif untuk mengembangkan budaya inovasi. c. Mewujudkan kualitas dosen dan tenaga kependidikan yang unggul berdasarkan nilai-nilai kebenaran dan kasih sayang. d. Mengoptimalkan civitas akademika dan pemangku kepentingan dalam melaksanakan tata kelola perguruan tinggi yang kredibel, transparan, akuntabel, bertanggung jawab, dan berkeadilan secara berkelanjutan. e. Membangun kemitraan dalam rangka meningkatkan kesejahteraan masyarakat."],
    "apa visi dan misi kampus darma cendika" : ["Untuk Visi dan Misi di kampus ukdc anda bisa mengakses link ini  https://ukdc.ac.id/visi-misi/"],
    "sebutkan visi kampus ukdc" : ["Visi : “Menjadi Universitas yang unggul dalam mengembangkan characterpreneurship di Indonesia."],
    "sebutkan misi kampus ukdc": ["Misi :Menyelenggarakan pendidikan tinggi yang integratif guna menghasilkan lulusan yang berkarakter wirausaha yang jujur, peduli dan bertanggung jawab. b. Menciptakan ekosistem pendidikan yang kolaboratif dan kondusif untuk mengembangkan budaya inovasi. c. Mewujudkan kualitas dosen dan tenaga kependidikan yang unggul berdasarkan nilai-nilai kebenaran dan kasih sayang. d. Mengoptimalkan civitas akademika dan pemangku kepentingan dalam melaksanakan tata kelola perguruan tinggi yang kredibel, transparan, akuntabel, bertanggung jawab, dan berkeadilan secara berkelanjutan. e. Membangun kemitraan dalam rangka meningkatkan kesejahteraan masyarakat."],
    "sebutkan visi dan misi kampus ukdc" : ["Untuk Visi dan Misi di kampus ukdc anda bisa mengakses link ini : https://ukdc.ac.id/visi-misi/"],

    "syarat" :["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "persyaratan masuk": ["Untuk mendaftar sebagai mahasiswa baru, Anda perlu memiliki ijazah SMA atau setara, mengisi formulir pendaftaran, melampirkan dokumen yang diperlukan, dan lulus dalam tahap seleksi. Informasi lebih lanjut dapat ditemukan di situs web resmi kami <a href='www.ukdc.ac.id'>halaman biaya kuliah</a>."],
    "saya ingin masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa saja untuk masuk ke ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat syarat ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa untuk masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya ingin masuk UKDC" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat syarat masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat syarat masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "apa syarat untuk masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],    
    "apa saja syarat syarat untuk masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "Sebutkan syarat apa saja yang ada di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya mau masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya mau masuk ukdc, bagaimana caranya" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya ingin masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya ingin masuk ukdc, bagaimana caranya" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "bagaimana cara saya masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "bagaimana caranya saya masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa saja untuk masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa saja untuk masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "persyaratan pendaftaran" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "persyaratan pendaftaran di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "persyaratan pendaftaran ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    
    
    
    "info pendaftaran" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "info pendafaran di ukdc" :["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "informasi pendaftaran" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "informasi pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaiamana cara mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "cara mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftar di UKDC" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftarkan diri" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftarkan diri di ukdc" :  ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau mendaftar" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar di ukdc, bagaimana caranya" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar di ukdc, bagaimana prosesnya" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "apakah saya bisa mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Pendaftaran di kampus UKDC" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Pendaftaran di univeristas UKDC" :["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Pendaftaran di univeristas UKDC" :["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Bagaimana mendaftar di kampus ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Bagaimana daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "cara saya masuk ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaimana cara untuk masuk ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaimana cara masuk ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaimana cara saya masuk ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaimana proses pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "bagaimana pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "proses pendaftaran" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "Bagaiaman proses pendaftaran ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "langkah langkah pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "langkah langkah pendaftaran" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    


    
    "informasi formulir pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "informasi form pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran di ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "boleh minta formulir pendaftaran ukdc": ["Silahkan, formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "form pendaftaran ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "form pendaftaran": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "tampilkan formulir pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "tampilkan form pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "apakah ada formulir pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "Adakah formulir pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "Berikan saya formulir pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    

    "biaya" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "infromasi mengenai pembayaran kuliah" :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "bayar kuliah" :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view"],
    "cara bayar kuliah " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view  "],
    "pembayaran kuliah " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa biaya kuliah di ukdc " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa uang kuliah ukdc " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya kuliah" :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa biaya persemester di kampus ukdc": ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa biaya perkuliahan di ukdc" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya kampus" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya di ukdc" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya persemester" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya persemester di kampus ukdc" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya persemester di UKDC" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "infomasi biaya kuliah" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "Informasi biaya kuliah di ukdc" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "Tarif pendaftaran online" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "Tarif kuliah di ukdc" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],



    #Proses Penerimaan Mahasiswa Baru
    "PMB UKDC" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "proses penerimaan": ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "bagaimana proses penerimaan di kampus UKDC" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],  
    "bagaimana proses penerimaan mahasiswa baru di kampus ukdc" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "proses penerimaan mahasiswa baru di kampus ukdc" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "proses penerimaan di kampus UKDC" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "bagaimana proses penerimaan di kampus UKDC" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "tahan dan proses PMB di kampus ukdc" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "bagaimana proses penerimaan mahasiswa baru di universitas katolik darma cendika" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "bagaimana tahap penerimaan mahasiswa baru di universitas katolik darma cendika" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "tahap tahap penerimaan mahasiswa baru di universitas katolik darma cendika" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "tahap tahap penerimaan mahasiswa baru di kampus ukdc" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "proses penerimaan mahasiswa baru" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "tahapan penerimaan mahasiswa baru" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],
    "tahap tahap penerimaan mahasiswa baru" : ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan berbagai tes. salah satunya adalah tes pengetahuan dan tes wawancara."],

    
    
    "jadwal penerimaan": ["Jadwal penerimaan mahasiswa baru kami biasanya dibuka setiap tahun pada bulan Mei dan ditutup pada bulan Agustus. Pastikan untuk memeriksa situs web resmi kami atau menghubungi bagian penerimaan untuk mendapatkan tanggal-tanggal penting, Informasi lebih lanjut dapat ditemukan di situs web resmi kami (https://www.ukdc.ac.id)."],
    "biaya kuliah": ["Biaya kuliah di universitas kami bervariasi tergantung pada program studi yang Anda pilih. Informasi lebih lanjut tentang biaya kuliah dan komponennya dapat ditemukan di brosur penerimaan atau Kunjungi [situs web resmi universitas kami](https://www.ukdc.ac.id) untuk informasi lebih lanjut."],
    "beasiswa": ["Kami menyediakan berbagai program beasiswa untuk mahasiswa baru yang berprestasi. Informasi tentang syarat dan pendaftaran beasiswa dapat ditemukan di kantor penerimaan atau situs web resmi kami di (https://www.ukdc.ac.id)."],
    "prodi favorit": ["Program studi yang paling diminati oleh mahasiswa baru kami umumnya adalah Teknik Informatika, Manajemen Bisnis, dan Psikologi. Namun, pilihan dapat bervariasi sesuai dengan minat masing-masing calon mahasiswa."],
    "pendaftaran online": ["Ya, kami menyediakan opsi pendaftaran online untuk memudahkan calon mahasiswa baru. Anda dapat mengunjungi situs web resmi kami dan mengikuti panduan pendaftaran online di sana."],
    "interview": ["Tidak semua program studi memerlukan sesi wawancara, tetapi beberapa program khusus atau beasiswa mungkin melibatkan wawancara sebagai bagian dari seleksi. Pastikan untuk memeriksa informasi pendaftaran atau menghubungi bagian penerimaan untuk detail lebih lanjut."],
    "peringkat universitas": ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],
    "peringkat universitas UKDC" : ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],
    "peringkat kampus UKDC" : ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],
    "peringkat kampus Univeristas Katolik Darma Cendika" : ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],
    "peringkat univ UKDC" : ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],
    "peringkat Univeristas Katolik Darma Cendika" : ["Universitas kami menempati peringkat 357 Indonesia, 4744 Asia serta peringkat 11548 dunia. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas. https://ukdc.ac.id/"],


    "fasilitas kampus": ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas apa saja yang ada di kampus UKDC": ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas apa saja yang ada di UKDC" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas apa saja yang ada di kampus UKDC" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "sebutkan fasilitas apa saja yang ada di kampus ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "sebutkan fasilitas apa saja yang ada di ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "kampus ukdc memiliki fasilitas apa saja" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "sebut dan jelaskan fasilitas di kampus ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas kampus ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],


    #Default untuk jawaban dari pertanyaan yang tidak ada di dataset
    "default" : ["Apakah ada sesuatu yang anda ingin tanyakan kepada saya? contoh : apa syarat masuk ukdc?, bagaiamana cara mendaftar di ukdc?, atau berapa uang kuliah di ukdc?"],



}

# Fungsi preprocessing
def preprocess_text(text):
    # Menghapus karakter non-alfabet
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Mengonversi teks menjadi huruf kecil
    text = text.lower()
    return text

    # Membuat objek stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # Stemming kata-kata
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return stemmed_tokens

# Proses preprocessing pada setiap nilai dalam kamus
preprocessed_responses = {key: [preprocess_text(response) for response in responses[key]] for key in responses}

#Fungsi Tokenisasi
def tokenize_text(text):
    # Menggunakan tokenisasi kata dari NLTK
    tokens = word_tokenize(text)
    return tokens

# Preprocessing responses
preprocessed_responses = {key: [tokenize_text(preprocess_text(response)) for response in responses[key]] for key in responses}


# Fungsi stemming
def stem_text(text):
    # Tokenisasi kata menggunakan nltk
    tokens = word_tokenize(text)

    # Inisialisasi PorterStemmer
    stemmer = PorterStemmer()

    # Melakukan stemming pada setiap token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Menggabungkan kembali token-token yang telah distem
    stemmed_text = ' '.join(stemmed_tokens)

    return stemmed_text

# Melakukan stemming pada setiap nilai dalam kamus
stemmed_responses = {key: [stem_text(response) for response in responses[key]] for key in responses}

# Fungsi untuk mendapatkan waktu saat ini di Jakarta
def get_current_time_jakarta():
    jakarta_timezone = pytz.timezone('Asia/Jakarta')
    now_jakarta = datetime.now(jakarta_timezone)
    current_time_jakarta = now_jakarta.strftime("%H:%M:%S")
    return current_time_jakarta

# Fungsi untuk mendapatkan nama hari saat ini dalam bahasa Indonesia
def get_current_hari():
    now = datetime.now()
    day_names = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    current_hari = day_names[now.weekday()]
    return current_hari
    
def get_current_tanggal():
    now = datetime.now()
    current_tanggal = now.strftime("%d")
    return current_tanggal

# Fungsi untuk mendapatkan bulan saat ini
def get_current_bulan():
    now = datetime.now()
    current_bulan = now.strftime("%m")
    return current_bulan

# Fungsi untuk mendapatkan tahun saat ini
def get_current_tahun():
    now = datetime.now()
    current_tahun = now.strftime("%Y")
    return current_tahun

# Fungsi untuk merespons pertanyaan pengguna
def respond(user_message, threshold=3):
    user_message = preprocess_text(user_message.lower())

    # Menanggapi pertanyaan tentang jam, hari, bulan, atau tahun
    date_time_response = handle_date_time_queries(user_message)
    if date_time_response:
        return date_time_response

    matched_keys = [key for key in responses if Levenshtein.distance(key, user_message) < threshold]

    # Jika ada kunci yang cocok, pilih respons dari salah satu kunci yang cocok
    if matched_keys:
        return random.choice(responses[random.choice(matched_keys)])
    else:
        return default_response()
        
# Menanggapi pertanyaan tentang jam, hari, bulan, atau tahun
def handle_date_time_queries(user_message):
    if 'jam' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang jam {get_current_time_jakarta()}."
    elif 'hari' in user_message and ('apa' in user_message or 'sekarang' in user_message):
        return f"Sekarang hari {get_current_hari()}."
    elif 'tanggal' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang tanggal {get_current_tanggal()}."
    elif 'bulan' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang bulan {get_current_bulan()}."
    elif 'tahun' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang tahun {get_current_tahun()}."
    else:
        return None

# Jika tidak ada kunci yang cocok, gunakan respons default
def default_response():
    return random.choice(responses["default"])



# Menyiapkan area untuk menampilkan percakapan
chat_area = st.empty()

#Direktori url pdf
syarat_pendaftaran = "https://penmaru.ukdc.ac.id/?page_id=25"
biaya_pendidikan = "https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view?usp=sharing"
formulir_pendaftaran= "https://docs.google.com/spreadsheets/u/1/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit?usp=sharing&ouid=113410767803438705296&rtpof=true&sd=true"
pendaftaran_online = "https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"


# Judul di sidebar
st.sidebar.markdown(f"""
<div style="text-align: center;">
    <h2>SI DARMA BOT </h2>
</div>
""", unsafe_allow_html=True)

user_name = st.sidebar.text_input("Nama Pengguna", "")

st.sidebar.markdown(f"""
<div style="text-align: center;">
    <h2>Selamat Datang {user_name} ! </h2>
</div>
""", unsafe_allow_html=True)

# Membuat garis di sidebar
st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="text-align: center;">
    <h2>Opsi Chatbot</h2>
</div>
""", unsafe_allow_html=True)


# Menambahkan beberapa pilihan dalam sidebar
show_image_option = st.sidebar.checkbox("Tampilkan Informasi Pendaftaran", True)

if show_image_option:
    st.sidebar.markdown(f"[Syarat Pendaftaran]({syarat_pendaftaran})")
    st.sidebar.markdown(f"[Flayer Biaya pendidikan]({biaya_pendidikan})")
    st.sidebar.markdown(f"[Form Pendaftaran]({formulir_pendaftaran})")
    st.sidebar.markdown(f"[Pendaftaran Online]({pendaftaran_online})")

    

# Menambahkan informasi tambahan atau tautan
st.sidebar.subheader("Informasi Tambahan")
st.sidebar.info("Si Darma Chatbot Adalah Sistem informasi ChatBot untuk membantu user dalam mencari informasi mengenai Universitas Katolik Darma Cendika.")

# Menambahkan tautan ke dokumentasi atau sumber daya
st.sidebar.subheader("Mari Tour Bersama Ku Di Kampus UKDC")
st.sidebar.markdown("[virtual Campus Tour 360](https://ukdc.ac.id/virtual-campus-tour-360/)")

# Menambahkan footer atau tanda air
st.sidebar.markdown("---")
st.sidebar.text("© 2024 Si Darma Chatbot UKDC")



conversation = []

# Inisialisasi percakapan pada sesi pertama (Inisialisasi session_state) 
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Form untuk input pengguna
with st.form(key='my_form'):
    user_message = st.text_input("Anda:", value="").lower()

    # Tombol kirim
    submit_button = st.form_submit_button("Kirim")

# Tanggapan jika tombol kirim ditekan
if submit_button:
    # Keluar dari chatbot jika input "exit"
    if user_message == "exit":
        st.success("Terima kasih telah menggunakan layanan chatbot kami")
    else:
        # Menambahkan pesan pengguna ke dalam percakapan
        st.session_state.conversation.append({"role": "Anda", "message": user_message})

        # Mendapatkan tanggapan dari chatbot
        bot_response = respond(user_message)

        # Menambahkan pesan bot ke dalam percakapan
        st.session_state.conversation.append({"role": "Darma Bot", "message": bot_response})

        # Mengosongkan nilai input setelah tombol diklik
        st.empty()

# Menampilkan chat history
for message in st.session_state.conversation:
    role = message['role']
    emoji = "👤" if role == "Anda" else "🤖"
    st.markdown(f"**{emoji} {role.capitalize()}**: {message['message']}") 
