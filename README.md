# DiaDetect – Sistem Prediksi Diabetes Menggunakan Machine Learning
**DiaDetect** adalah sistem prediksi risiko diabetes yang dibangun menggunakan model machine learning berbasis dataset kesehatan. Proyek ini bertujuan untuk membantu dalam deteksi dini risiko diabetes dengan menggunakan data indikator kesehatan.

## 🔍 Deskripsi Proyek
DiaDetect memanfaatkan model machine learning untuk memprediksi kemungkinan seseorang mengidap diabetes berdasarkan indikator kesehatan yang tersedia dalam dataset. Proyek ini dirancang untuk memberikan wawasan awal mengenai potensi risiko diabetes, yang dapat digunakan sebagai alat bantu dalam pengambilan keputusan medis.

## ⚙️ Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama yang digunakan dalam pengembangan model dan aplikasi.
- **Streamlit**: Digunakan untuk membangun antarmuka pengguna (UI) berbasis web yang interaktif untuk visualisasi hasil prediksi dan data.
- **TensorFlow / Keras**: Digunakan untuk membangun dan melatih model machine learning.
- **Jupyter Notebook**: Digunakan untuk eksplorasi data dan pengembangan model secara interaktif.
- **Scikit-learn**: Digunakan untuk preprocessing data dan evaluasi model.

## 📁 Struktur Proyek
```
DiaDetect/
├── 📁 assets/                     # Berisi file pendukung seperti gambar atau dokumentasi tambahan
├── 📄 app.py                      # Aplikasi Streamlit yang menghandle UI dan prediksi
├── 📄 diabetes\_model.h5           # Model machine learning yang telah dilatih
├── 📄 diabetes\_012\_health\_indicators\_BRFSS2015.csv  # Dataset yang digunakan untuk pelatihan model
├── 📄 requirements.txt            # Daftar dependensi Python yang diperlukan
├── 📄 DiaDetect.ipynb             # Notebook Jupyter untuk eksplorasi data dan pengembangan model
└── 📄 .devcontainer/              # Konfigurasi untuk pengembangan dalam container
```

## 📊 Kredit Dataset
Dataset yang digunakan dalam proyek ini diambil dari [Kaggle - Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset). Dataset ini berisi berbagai indikator kesehatan yang digunakan untuk memprediksi risiko diabetes.

## 🧪 Eksplorasi Data dan Pengembangan Model
Gunakan Jupyter Notebook `DiaDetect.ipynb` untuk eksplorasi data, visualisasi, dan pengembangan model machine learning. Notebook ini menyediakan langkah-langkah untuk memahami dataset dan membangun model prediksi.
