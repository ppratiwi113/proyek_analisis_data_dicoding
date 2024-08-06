# Proyek Analisis Data Python - DICODING
Proyek ini adalah bagian dari program pelatihan data science di Dicoding. Dalam proyek ini, kami menganalisis data penyewaan sepeda untuk memahami tren dan pola dalam penggunaan sepeda berdasarkan faktor-faktor seperti cuaca, musim, dan jenis pengguna.

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda selama periode waktu tertentu. Data ini mencakup informasi seperti jumlah penyewaan harian dan per jam, kondisi cuaca, suhu, kecepatan angin, dan kategori pengguna (casual dan registered).

## Fitur
- **Visualisasi Tren Penyewaan**: Memvisualisasikan tren penyewaan sepeda berdasarkan waktu (bulanan, harian, dan per jam).
- **Analisis Pengguna**: Membedakan pola penyewaan antara pengguna casual dan registered.
- **Dampak Cuaca**: Menentukan bagaimana kondisi cuaca mempengaruhi jumlah penyewaan sepeda.

## Instalasi
1. Clone repository ini:
   ```bash
   git clone https://github.com/ppratiwi113/proyek_analisis_data_dicoding.git

2. Masuk ke direktori proyek:
    ```bash
    cd proyek_analisis_data_dicoding

3. Instalasi dependecies:
    ```bash
    pip install streamlit
    pip install -r requirements.txt

## Penggunaan
1. Ubah ke direktori proyek (Local):

    ```bash
    cd .\Dashboard\
    streamlit run dashboard.py
    ```
2. Buka browser dan akses http://localhost:8501 untuk melihat dashboard.

    Atau bisa dengan kunjungi website ini [Project Data Analytics](https://bike-sharing-ariniamsr.streamlit.app/)

## Struktur Proyek
- dashboard.py: Script utama untuk menjalankan dashboard Streamlit
- cleaned_day.csv dan cleaned_hour.csv: Dataset yang digunakan untuk pembuatan dashboard.py
- day.csv dan hour.csv: Dataset awal sebelum di perbaharui
- Proyek_Analisis_Data.ipynb: Notebook Jupyter yang berisi analisis dan visualisasi data

## Hasil Analisis
Beberapa temuan utama dari analisis ini meliputi:

- Tren Musiman: Jumlah penyewaan sepeda cenderung meningkat pada musim panas dan menurun pada musim dingin.
- Dampak Cuaca dan Musim: Kondisi cuaca seperti hujan dan kabut secara signifikan mengurangi jumlah penyewaan.
- Pola Pengguna: Pengguna registered lebih aktif pada hari kerja, sementara pengguna casual lebih banyak menyewa pada akhir pekan.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka issue untuk mendiskusikan perubahan yang ingin Anda lakukan.

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file `LISENCE` untuk detail lebih lanjut.


