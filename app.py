import streamlit as st
import numpy as np
import pandas as pd
import string
import random
import Levenshtein
import re
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from datetime import datetime
import locale
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
nltk.download('punkt')
nltk.download('stopwords')



# Path gambar background
background_image_path = "/app/bot.webp"  # Ganti dengan path gambar Anda

# Menambahkan gambar sebagai background dengan lebar 100%
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_image_path}');

    }}
    </style>
    """,
    unsafe_allow_html=True
)


# with open("D:/TUGAS AKHIR/desain.html", "r") as file:
#     html_code = file.read()

# print(html_code)

import streamlit as st

# Judul di tengah dengan HTML
# Path gambar
# Path gambar
image_path = "/app/chatbot.webp"  # Ganti dengan path gambar Anda

# Menambahkan gambar di halaman utama
st.image(image_path, width=100)

# Menambahkan judul di halaman utama
st.markdown("<h1 style='text-align: center;'>SI Darma Chatbot</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Halo! nama aku darma bot, Silahkan Ajukan Pertanyaan Anda!</p>", unsafe_allow_html=True)



#pertanyaan dan jawaban
responses = {

    "pagi" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi kawan" : ["Selamat Pagi , Ada yang bisa saya bantu?"],
    "selamat pagi teman" : ["Selamat Pagi , Ada yang bisa saya bantu?"],

    "siang" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang kawan" : ["Selamat Siang , Ada yang bisa saya bantu?"],
    "selamat siang teman" : ["Selamat Siang , Ada yang bisa saya bantu?"],

    "sore" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore kawan" : ["Selamat Sore , Ada yang bisa saya bantu?" ],
    "selamat sore teman" : ["Selamat Sore , Ada yang bisa saya bantu?" ],

    "malam" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam kawan" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam teman" : ["Selamat Malam , Ada yang bisa saya bantu?"],
    "selamat malam" : ["Selamat Malam , Ada yang bisa saya bantu?"],

    "hai" : ["Hai, ada yang bisa saya bantu?"],
    "halo" :["Halo , ada yang bisa saya bantu?"],
    "hallo" :["Halo , ada yang bisa saya bantu?"],
    "hi" : ["Hi, ada yang bisa saya bantu?"],
    "hay" : ["Hay, ada yang bisa saya bantu?"],
    "hy" : ["Hy, ada yang bisa saya bantu?"],

    "hai darma bot" : ["Hai, ada yang bisa saya bantu?"],
    "halo darma bot" :["Halo, ada yang bisa saya bantu?"],
    "hallo darma bot" :["Halo, ada yang bisa saya bantu?"],
    "hi darma bot" : ["Hi, ada yang bisa saya bantu?"],
    "hay darma bot" : ["Hay, ada yang bisa saya bantu?"],
    "hy darma bot" : ["Hy, ada yang bisa saya bantu?"],



    "hai bot" : ["Hai, ada yang bisa saya bantu?"],
    "halo bot" :["Halo, ada yang bisa saya bantu?"],
    "hallo bot" :["Halo, ada yang bisa saya bantu?"],
    "hi bot" : ["Hi, ada yang bisa saya bantu?"],
    "hay bot" : ["Hay, ada yang bisa saya bantu?"],
    "hy bot" : ["Hy, ada yang bisa saya bantu?"],

    "hai kawan" : ["Hai, ada yang bisa saya bantu?"],
    "halo kawan " :["Halo, ada yang bisa saya bantu?"],
    "hallo kawan " :["Halo, ada yang bisa saya bantu?"],
    "hi kawan " : ["Hi, ada yang bisa saya bantu?"],
    "hay kawan " : ["Hay, ada yang bisa saya bantu?"],
    "hy kawan " : ["Hy, ada yang bisa saya bantu?"],

    "hai teman" : ["Hai, ada yang bisa saya bantu?"],
    "halo teman" :["Halo, ada yang bisa saya bantu?"],
    "hallo teman" :["Halo, ada yang bisa saya bantu?"],
    "hi teman" : ["Hi, ada yang bisa saya bantu?"],
    "hay teman" : ["Hay, ada yang bisa saya bantu?"],
    "hy teman" : ["Hy, ada yang bisa saya bantu?"],

    "hai bot" : ["Hai, ada yang bisa saya bantu?"],
    "halo bot" :["Halo, ada yang bisa saya bantu?"],
    "hallo bot" :["Halo, ada yang bisa saya bantu?"],
    "hi bot" : ["Hi, ada yang bisa saya bantu?"],
    "hay bot" : ["Hay, ada yang bisa saya bantu?"],
    "hy bot" : ["Hy, ada yang bisa saya bantu?"],

    "salam": ["Salam juga!", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "kenal" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "salam kenal ya" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "salam kenal" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],

    "sip": ["Salam juga!", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "iya" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "oke" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    "okeh" : ["Salam kenal juga", "Senang bertemu dengan Anda.", "Hai, apa kabar?"],
    

    "baik" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "sehat" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Alhamdullilah, sehat": ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Alhamdullilah, baik": ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Puji tuhan, baik" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],
    "Puji tuhan, sehat" : ["Syukurlah semoga sehat selalu ya, Ada yang bisa saya bantu? "],

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

    "terimakasih" : ["Baik, sama-sama"],
    "makasih" : ["Baik, sama-sama"],
    "terimakasih ya" : ["Baik, sama-sama"],
    "makasih ya" : ["Baik, sama-sama"],

    "bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya ingin bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "saya mau bertanya" :["Silahkan","Apa yang anda ingin tanyakan?"],
    "mau tanya tanya" :["Silahkan"],
    "saya mau tanya tanya" :["Silahkan"],
    "saya mau tanya" :["Silahkan","Apa yang anda ingin tanyakan?"],

    "siapa kamu"  : ["Saya adalah Darma Bot","Saya adalah bot"],
    "nama kamu siapa"  : ["Saya adalah Darma Bot","Saya adalah bot"],
    "siapa nama kamu"  : ["Saya adalah Darma Bot","Saya adalah bot"],
    "kamu siapa" :  ["Saya adalah Darma Bot","Saya adalah bot"],
    "kamu itu siapa" :  ["Saya adalah Darma Bot","Saya adalah bot"],
    "siapa kamu itu" :  ["Saya adalah Darma Bot","Saya adalah bot"],
    "nama": ["Saya adalah Chatbot Darma.", "Anda bisa memanggil saya Darma.", "Salam kenal!"],

    "jurusan ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan apa saja yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi apa saja yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "prodi yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],
    "jurusan apa yang ada di ukdc" : ["1.Prodi Manajemen 2.Prodi Akutansi 3.Prodi Ilmu Hukum 4.Prodi Teknik Industri 5.Prodi Teknik Informatika 6.Prodi Arsitektur 7.Prodi Akupuntur & Pengobatan Herbal"],

    "syarat" :["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya ingin masuk ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa saja untuk masuk ke ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat syarat ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat apa untuk masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "syarat masuk di ukdc" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],
    "saya ingin masuk UKDC" : ["Anda dapat melihat syarat pendaftaran di https://penmaru.ukdc.ac.id/?page_id=25"],

    "bagaiamana cara mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau daftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "cara mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "pendaftaran di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya mau mendaftar di ukdc" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftar di UKDC" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftarkan diri" : ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],
    "saya ingin mendaftarkan diri di ukdc" :  ["Anda dapat mengakses jalur pendaftaran di https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"],


    "pendaftaran" : ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran di ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "formulir pendaftaran ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "boleh minta formulir pendaftaran ukdc": ["Silahkan, formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "form pendaftaran ukdc": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],
    "form pendaftaran": ["Formulir pendaftaran ada di https://docs.google.com/spreadsheets/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit#gid=136700603"],

    "biaya" : ["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "infromasi mengenai pembayaran kuliah" :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "bayar kuliah" :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view"],
    "cara bayar kuliah " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view  "],
    "pembayaran kuliah " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa biaya kuliah di ukdc " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "berapa uang kuliah ukdc " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],
    "biaya kuliah " :["Kalian bisa langsung download flyer ini ya https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view "],

    "proses penerimaan": ["Proses penerimaan mahasiswa baru di universitas kami melibatkan beberapa tahap, termasuk pengisian formulir, pengumpulan dokumen, dan wawancara."],
    "persyaratan masuk": ["Untuk mendaftar sebagai mahasiswa baru, Anda perlu memiliki ijazah SMA atau setara, mengisi formulir pendaftaran, melampirkan dokumen yang diperlukan, dan lulus dalam tahap seleksi. Informasi lebih lanjut dapat ditemukan di situs web resmi kami <a href='www.ukdc.ac.id'>halaman biaya kuliah</a>."],
    "jadwal penerimaan": ["Jadwal penerimaan mahasiswa baru kami biasanya dibuka setiap tahun pada bulan Mei dan ditutup pada bulan Agustus. Pastikan untuk memeriksa situs web resmi kami atau menghubungi bagian penerimaan untuk mendapatkan tanggal-tanggal penting, Informasi lebih lanjut dapat ditemukan di situs web resmi kami (https://www.ukdc.ac.id)."],
    "biaya kuliah": ["Biaya kuliah di universitas kami bervariasi tergantung pada program studi yang Anda pilih. Informasi lebih lanjut tentang biaya kuliah dan komponennya dapat ditemukan di brosur penerimaan atau Kunjungi [situs web resmi universitas kami](https://www.ukdc.ac.id) untuk informasi lebih lanjut."],
    "beasiswa": ["Kami menyediakan berbagai program beasiswa untuk mahasiswa baru yang berprestasi. Informasi tentang syarat dan pendaftaran beasiswa dapat ditemukan di kantor penerimaan atau situs web resmi kami di (https://www.ukdc.ac.id)."],
    "prodi favorit": ["Program studi yang paling diminati oleh mahasiswa baru kami umumnya adalah Teknik Informatika, Manajemen Bisnis, dan Psikologi. Namun, pilihan dapat bervariasi sesuai dengan minat masing-masing calon mahasiswa."],
    "pendaftaran online": ["Ya, kami menyediakan opsi pendaftaran online untuk memudahkan calon mahasiswa baru. Anda dapat mengunjungi situs web resmi kami dan mengikuti panduan pendaftaran online di sana."],
    "interview": ["Tidak semua program studi memerlukan sesi wawancara, tetapi beberapa program khusus atau beasiswa mungkin melibatkan wawancara sebagai bagian dari seleksi. Pastikan untuk memeriksa informasi pendaftaran atau menghubungi bagian penerimaan untuk detail lebih lanjut."],
    "peringkat universitas": ["Universitas kami memiliki peringkat yang sangat baik di tingkat nasional dan regional. Untuk informasi lebih lanjut tentang peringkat kami, Anda dapat merujuk ke lembaga penilaian pendidikan resmi atau situs web resmi universitas."],
    
    "fasilitas kampus": ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas apa saja yang ada di kampus UKDC": ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],
    "fasilitas ukdc" : ["Kampus kami dilengkapi dengan berbagai fasilitas untuk mendukung kegiatan belajar-mengajar dan kehidupan mahasiswa. Ini termasuk perpustakaan yang baik, laboratorium hardware komputer, dan fasilitas olahraga. Anda dapat mengunjungi kampus kami untuk tur lebih lanjut."],

    #Default untuk jawaban dari pertanyaan yang tidak ada di dataset
    "default" : ["Apakah ada sesuatu yang anda ingin tanyakan kepada saya? saya disni untuk membantu. Ada yang bisa saya bantu?"],



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

def get_current_time():
    # Fungsi untuk mendapatkan waktu saat ini
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_current_hari():
    # Set locale ke bahasa Indonesia
    locale.setlocale(locale.LC_TIME, 'id_ID')

    # Fungsi untuk mendapatkan nama hari saat ini
    now = datetime.now()
    current_hari = now.strftime("%A")

    # Kembalikan locale ke setting awal (default)
    locale.setlocale(locale.LC_TIME, '')

    return current_hari

def get_current_tanggal():
    # Fungsi untuk mendapatkan tanggal saat ini
    now = datetime.now()
    current_date = now.strftime("%d")
    return current_date
def get_current_bulan():
    # Fungsi untuk mendapatkan bulan saat ini
    now = datetime.now()
    current_date = now.strftime("%m")
    return current_date
def get_current_tahun():
    # Fungsi untuk mendapatkan tahun saat ini
    now = datetime.now()
    current_date = now.strftime("%Y")
    return current_date


def respond(user_message, threshold = 3):
    user_message = preprocess_text(user_message.lower())



    matched_keys = [key for key in responses if Levenshtein.distance(key, user_message) < threshold]

    # Jika ada kunci yang cocok, pilih respons dari salah satu kunci yang cocok
    if matched_keys:
        return random.choice(responses[random.choice(matched_keys)])
    else:
        return random.choice(responses["default"])


    # Menanggapi pertanyaan tentang jam
    if 'jam' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang jam {get_current_time()}."

    # Menanggapi pertanyaan tentang hari
    if 'hari' in user_message and ('apa' in user_message or 'sekarang' in user_message):
        return f"Sekarang hari {get_current_hari()}."

    # Menanggapi pertanyaan tentang tanggal
    if 'tanggal' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang tanggal {get_current_tanggal()}."

    # Menanggapi pertanyaan tentang tanggal
    if 'bulan' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang bulan {get_current_bulan()}."

    # Menanggapi pertanyaan tentang tanggal
    if 'tahun' in user_message and ('berapa' in user_message or 'sekarang' in user_message):
        return f"Sekarang tahun {get_current_tahun()}."
    
    
    
        # Jika tidak ada kunci yang cocok, gunakan respons default
    else :
        return random.choice(responses["default"])



# Menyiapkan area untuk menampilkan percakapan
chat_area = st.empty()

#Direktori url pdf
syarat_pendaftaran = "https://penmaru.ukdc.ac.id/?page_id=25"
biaya_pendidikan = "https://drive.google.com/file/d/1cEGxjDqxJWdZqK3Hi4ETOedWXpsgQKHw/view?usp=sharing"
formulir_pendaftaran= "https://docs.google.com/spreadsheets/u/1/d/1E1TholuFMoD1Vrv8oqZLaLGB_eGftI3L/edit?usp=sharing&ouid=113410767803438705296&rtpof=true&sd=true"
pendaftaran_online = "https://siakad.ukdc.ac.id/spmbfront/jalur-seleksi"

# Percakapan antara pengguna dan chatbot
conversation = []


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
st.sidebar.subheader("Sumber Daya")
st.sidebar.markdown("[Dokumentasi Chatbot](https://example.com/docs)")

# Menambahkan footer atau tanda air
st.sidebar.markdown("---")
st.sidebar.text("© 2024 Si Darma Chatbot UKDC")



user_message = st.text_input("Anda:", value="", key="user_input").lower()


# Tombol kirim
if st.button("Kirim"):
    # Keluar dari chatbot jika input "exit"
    if user_message == "exit":
        st.success("Terima kasih telah menggunakan layanan chatbot kami")
    else:
        # Menambahkan pesan pengguna ke dalam percakapan
        conversation.append({"role": "Anda", "message": user_message})
        
        # Mendapatkan tanggapan dari chatbot
        bot_response = respond(user_message)
        
        # Menambahkan pesan bot ke dalam percakapan
        conversation.append({"role": "bot", "message": bot_response})

        user_message = ""

        

    chat_area.text("")
    for message in conversation:
        role = message['role'].capitalize()
        if role == 'Bot':
            st.markdown(f"**{role}** 🤖: {message['message']}")
        else:
            st.markdown(f"**{role}** 👤: {message['message']}")




