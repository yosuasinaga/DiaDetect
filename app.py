import streamlit as st
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

# Muat model yang telah disimpan
model = tf.keras.models.load_model('diabetes_model.h5')

# Standarisasi Data (Gunakan scaler yang sama seperti saat pelatihan)
scaler = StandardScaler()

# Fungsi untuk melakukan prediksi
def predict_diabetes(input_data):
    # Standarisasi data input
    input_df = pd.DataFrame(input_data, index=[0])
    columns_to_standardize = ['BMI', 'GenHlth', 'PhysHlth', 'Age', 'Education', 'Income']
    input_df[columns_to_standardize] = scaler.fit_transform(input_df[columns_to_standardize])
    
    # Prediksi dengan model
    predictions = model.predict(input_df)
    predicted_class = np.argmax(predictions)  # Mengambil kelas dengan probabilitas tertinggi
    return predicted_class

# Fungsi untuk mengonversi "Iya" menjadi 1 dan "Tidak" menjadi 0
def convert_to_numeric(value):
    return 1 if value == 'Iya' else 0

def convert_income(value): 
    if value == 'Kurang dari Rp1.000.000':
        return 1
    elif value == 'Rp1.000.000 - Rp2.500.000':
        return 2
    elif value == 'Rp2.500.000 - Rp5.000.000':
        return 3
    elif value == 'Rp5.000.000 - Rp10.000.000':
        return 4
    elif value == 'Rp10.000.000 - Rp20.000.000':
        return 5
    elif value == 'Rp20.000.000 - Rp35.000.000':
        return 6
    elif value == 'Rp35.000.000 - Rp85.000.000':
        return 7
    elif value == 'Lebih dari Rp85.000.000':
        return 8

def convert_education(value):
    if value == 'TK':
        return 1
    elif value == 'SD':
        return 2
    elif value == 'SMP':
        return 3
    elif value == 'SMA':
        return 4
    elif value == 'Diploma/Vokasi':
        return 5
    elif value == 'Sarjana':
        return 6
    
def convert_age(value):
    if value == '18-24':
        return 1
    elif value == '25-29':
        return 2
    elif value == '30-34':
        return 3
    elif value == '35-39':
        return 4
    elif value == '40-44':
        return 5
    elif value == '45-49':
        return 6
    elif value == '50-54':
        return 7
    elif value == '55-59':
        return 8
    elif value == '60-64':
        return 9
    elif value == '65-69':
        return 10
    elif value == '70-74':
        return 11
    elif value == '75-79':
        return 12
    elif value == '80+':
        return 13

def convert_gen_health(value):
    if value == 'Sangat Baik':
        return 1
    elif value == 'Baik':
        return 2
    elif value == 'Biasa':
        return 3
    elif value == 'Buruk':
        return 4
    elif value == 'Sangat Buruk':
        return 5

# Sidebar untuk navigasi
tab1, tab2, tab3 = st.tabs(["Home", "Mulai Tes", "Tentang Proyek"])

# Tab 1: Home
with tab1:
    # Menampilkan gambar SVG dari file lokal
    st.image("assets/logo.svg")
    st.write("""
    ## **Deskripsi Proyek**  
    **DiaDetect** merupakan aplikasi **prediksi risiko diabetes** yang dikembangkan dengan pendekatan **machine learning** berdasarkan data survei kesehatan **BRFSS2015** dari CDC. Aplikasi ini dirancang untuk memberikan kemudahan bagi masyarakat dalam melakukan **deteksi dini risiko diabetes**, tanpa perlu melalui prosedur medis yang kompleks. Dengan memanfaatkan indikator kesehatan seperti **BMI**, **tekanan darah**, **kolesterol**, dan **aktivitas fisik**, aplikasi ini memberikan prediksi yang informatif guna mendorong tindakan pencegahan sedini mungkin.

    ## **Tujuan Proyek**  
    Proyek ini bertujuan untuk menghadirkan solusi nyata atas permasalahan keterlambatan **deteksi dini risiko diabetes** di masyarakat. Melalui pemanfaatan teknologi **machine learning** dan data kesehatan yang valid, kami ingin membangun **model klasifikasi risiko dengan akurasi tinggi** untuk mengidentifikasi kondisi **tidak diabetes**, **prediabetes**, dan **diabetes**. Diharapkan, aplikasi ini dapat memberikan kontribusi nyata dalam mendukung **pengambilan keputusan preventif** oleh pengguna dan praktisi kesehatan.
    """)

    st.write("""
    ## **Fakta Menarik Tentang Diabetes**  
    - **Diabetes** adalah salah satu **penyakit kronis** yang berkembang pesat di dunia, dengan lebih dari **400 juta orang** yang menderita diabetes.  
    - Di **Indonesia**, lebih dari **10% populasi dewasa** mengalami diabetes atau prediabetes.  
    - Faktor risiko diabetes meliputi **usia**, **obesitas**, **kurangnya aktivitas fisik**, serta **pola makan yang tidak sehat**.  
    - Diabetes yang tidak terkontrol dapat menyebabkan masalah serius seperti **kebutaan**, **penyakit jantung**, **stroke**, dan **kerusakan ginjal**.
    """)

    st.write("""
    ## **Contoh Kasus Prediksi dan Manfaat**

    ### **Contoh Kasus**  
    Jika seseorang memiliki **BMI 30**, **tekanan darah tinggi**, dan **kolesterol tinggi**, aplikasi ini akan memberikan prediksi bahwa mereka **berisiko mengembangkan diabetes**. Dengan mengikuti saran untuk **menurunkan berat badan** dan **meningkatkan aktivitas fisik**, mereka bisa mengurangi risiko diabetes.

    ### **Manfaat Prediksi**
    - **Mencegah Diabetes**: Dengan mengetahui risiko diabetes, Anda bisa mengambil **langkah pencegahan lebih awal** untuk menjaga pola makan dan gaya hidup sehat.
    - **Pemantauan Kesehatan Rutin**: Dapat membantu Anda untuk lebih rutin **memantau kesehatan**, seperti memeriksa kadar gula darah secara teratur.

    ### **Mulai Tes Anda Sekarang!**
    """)

    # FAQ
    st.write("## **Pertanyaan yang Sering Diajukan**")
    with st.expander("**Apa itu prediksi diabetes?**"):
        st.write("**Prediksi diabetes** membantu Anda mengetahui apakah Anda **berisiko mengalami diabetes** berdasarkan data yang Anda berikan, seperti tekanan darah, kolesterol, BMI, dan faktor lainnya.")
    with st.expander("**Apa yang dimaksud dengan prediabetes?**"):
        st.write("**Prediabetes** adalah kondisi ketika kadar gula darah Anda lebih tinggi dari normal tetapi belum cukup tinggi untuk didiagnosis sebagai diabetes. Ini adalah kondisi yang dapat diubah dengan **gaya hidup sehat**.")
    with st.expander("**Apakah aplikasi ini menggantikan pemeriksaan medis?**"):
        st.write("**Tidak.** Aplikasi ini memberikan prediksi berdasarkan data yang dimasukkan, namun **sangat disarankan** untuk berkonsultasi dengan dokter untuk **diagnosa dan perawatan** yang lebih tepat.")
    with st.expander("**Apa yang harus saya lakukan jika aplikasi ini memprediksi saya memiliki diabetes?**"):
        st.write("Jika Anda terdiagnosa diabetes, penting untuk **mengatur pola makan**, **rutin memantau kadar gula darah**, serta mengikuti **anjuran pengobatan dari dokter** Anda.")



# Tab 2: Mulai Tes
with tab2:
    st.image("assets/logo.svg")
    st.title("Masukkan Data untuk Prediksi Diabetes")

    # Input data dari pengguna
    high_bp = st.selectbox('Apakah Anda memiliki tekanan darah tinggi?', ['Tidak', 'Iya'])
    high_chol = st.selectbox('Apakah Anda memiliki kolesterol tinggi?', ['Tidak', 'Iya'])
    bmi = st.number_input('BMI (Body Mass Index)', min_value=12.0, max_value=98.0, step=0.1)
    stroke = st.selectbox('Pernahkah Anda mengalami stroke?', ['Tidak', 'Iya'])
    heart_disease = st.selectbox('Apakah Anda memiliki penyakit jantung?', ['Tidak', 'Iya'])
    phys_activity = st.selectbox('Apakah Anda melakukan aktivitas fisik dalam 30 hari terakhir? (tidak termasuk bekerja)', ['Tidak', 'Iya'])
    gen_health = st.selectbox('Bagaimana kondisi kesehatan Anda secara umum?', ['Sangat Baik', 'Baik', 'Biasa', 'Buruk', 'Sangat Buruk'])
    phys_health = st.number_input('Dalam 30 hari terakhir, berapa jumlah hari dimana kesehatan fisik Anda merasa terganggu?', min_value=0, max_value=30, step=1)
    diff_walk = st.selectbox('Apakah Anda memiliki kesulitan berjalan atau menaiki tangga?', ['Tidak', 'Iya'])
    age = st.selectbox('Rentang Usia', ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+'])
    education = st.selectbox('Tingkat Pendidikan', ['TK', 'SD', 'SMP', 'SMA', 'Diploma/Vokasi', 'Sarjana'])
    income = st.selectbox('Pendapatan Bulanan', ['Kurang dari Rp1.000.000', 'Rp1.000.000 - Rp2.500.000', 'Rp2.500.000 - Rp5.000.000', 'Rp5.000.000 - Rp10.000.000', 'Rp10.000.000 - Rp20.000.000', 'Rp20.000.000 - Rp35.000.000', 'Rp35.000.000 - Rp85.000.000', 'Lebih dari Rp85.000.000'])

    # Data yang dimasukkan pengguna
    input_data = {
        'HighBP': [convert_to_numeric(high_bp)],
        'HighChol': [convert_to_numeric(high_chol)],
        'BMI': [bmi],
        'Stroke': [convert_to_numeric(stroke)],
        'HeartDiseaseorAttack': [convert_to_numeric(heart_disease)],
        'PhysActivity': [convert_to_numeric(phys_activity)],
        'GenHlth': [convert_gen_health(gen_health)],
        'PhysHlth': [phys_health],
        'DiffWalk': [convert_to_numeric(diff_walk)],
        'Age': [convert_age(age)],
        'Education': [convert_education(education)],
        'Income': [convert_income(income)]
    }

    if st.button('Prediksi'):
        result = predict_diabetes(input_data)

        with st.expander("Klik untuk melihat hasil prediksi"):
            if result == 0:
                st.write("**Anda terindikasi sehat dan tidak memiliki diabetes.**")
                st.write("**Saran**: Lanjutkan **gaya hidup sehat** dengan menjaga pola makan yang seimbang, rutin berolahraga, dan memeriksakan kesehatan secara berkala.")
                st.write("Tetap jaga pola hidup sehat dan hindari kebiasaan berisiko seperti **merokok** dan **konsumsi alkohol**.")

            elif result == 1:
                st.write("**Anda terindikasi prediabetes.**")
                st.write("**Saran**: Perubahan **pola makan** dan **gaya hidup** sangat penting untuk mencegah perkembangan menjadi diabetes. Pertimbangkan untuk makan lebih banyak **sayuran**, **buah**, dan makanan **rendah gula**.")
                st.write("Tingkatkan aktivitas fisik Anda, jaga berat badan, dan hindari makanan yang dapat meningkatkan kadar gula darah.")
                st.write("**Penting**: Segera lakukan pemeriksaan lebih lanjut dengan **dokter** untuk langkah pencegahan yang tepat.")

            else:
                st.write("**Anda terindikasi diabetes.**")
                st.write("**Saran**: **Perawatan diabetes sangat penting.** Pastikan untuk memantau kadar gula darah secara teratur dan mengikuti pengobatan yang dianjurkan oleh dokter.")
                st.write("Fokuslah pada **pola makan sehat**, **olahraga teratur**, dan **kontrol berat badan**. Ikuti anjuran medis dan lakukan pemeriksaan rutin.")
                st.write("**Penting**: **Berkonsultasilah dengan dokter** untuk mendapatkan perawatan yang tepat dan pertimbangkan bergabung dengan **kelompok dukungan** untuk penderita diabetes.")

# Tab 3: Tentang Proyek
with tab3:
    st.image("assets/logo.svg")
    st.title("Tentang DiaDetect")

    st.write("""
    **DiaDetect** adalah aplikasi **prediksi risiko diabetes** berbasis **machine learning** yang dikembangkan oleh tim mahasiswa sebagai bagian dari proyek **inovasi kesehatan**. Aplikasi ini menggunakan dataset **BRFSS2015** yang bersumber dari **Centers for Disease Control and Prevention (CDC)**, yang telah tersedia secara terbuka di Kaggle. Fokus utama pengembangan ini adalah untuk menciptakan **alat bantu skrining** yang cepat dan mudah digunakan oleh masyarakat luas tanpa perlu alat medis atau pemeriksaan laboratorium, dengan tetap mengutamakan **akurasi prediksi**.
    """)

    st.subheader("Latar Belakang Proyek")
    st.write("""
    Dengan meningkatnya jumlah penderita diabetes di seluruh dunia, terutama di Indonesia, aplikasi ini hadir untuk membantu individu memahami **risiko kesehatan** mereka. Proyek ini menggunakan **model machine learning** yang sudah terlatih untuk memprediksi apakah seseorang berisiko mengembangkan diabetes berdasarkan **data yang mereka masukkan**.
    """)

    st.subheader("Arsitektur Model")
    st.write("""
    **Model machine learning** yang digunakan dalam DiaDetect dibangun dari nol menggunakan **TensorFlow** dan **Scikit-Learn**. Proses pengembangan diawali dengan **eksplorasi data** dan **feature engineering** berdasarkan 12 variabel kesehatan dalam dataset.

    Model klasifikasi yang digunakan dikembangkan dalam **klasifikasi multi-kelas** (*tidak diabetes, prediabetes, diabetes*). Untuk meningkatkan performa, model dituning dengan metode **hyperparameter tuning** dan evaluasi dilakukan dengan berbagai metrik:

    - **Akurasi** – untuk mengukur proporsi prediksi yang benar  
    - **Presisi** – untuk mengukur ketepatan prediksi positif  
    - **Recall** – untuk mengukur sensitivitas terhadap kasus positif  
    - **F1-Score** – gabungan presisi dan recall sebagai metrik keseimbangan  

    Dataset yang digunakan adalah *Behavioral Risk Factor Surveillance System (BRFSS) 2015* yang tersedia secara publik di Kaggle:  
    - [**BRFSS Diabetes Dataset – Kaggle**](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

    Seluruh model disimpan dalam format **`.h5`** untuk digunakan pada aplikasi ini secara lokal, dan diproses menggunakan environment **Google Colab**.
    """)

    st.subheader("Evaluasi Model")
    st.write("""
    **Model terbaik** yang digunakan dalam aplikasi DiaDetect dievaluasi menggunakan data validasi terpisah. Berikut adalah hasil metrik evaluasi pada skema klasifikasi multi-kelas:

    - **Akurasi**: **52%**  
    - **Presisi (macro average)**: **54%**  
    - **Recall (macro average)**: **53%**  
    - **F1-Score (macro average)**: **52%**  

    Hasil evaluasi ini menunjukkan bahwa model masih memiliki **keterbatasan** dalam membedakan secara optimal antara ketiga kelas risiko diabetes. Meskipun demikian, model sudah mampu memberikan **gambaran awal** mengenai risiko yang mungkin dihadapi oleh pengguna. Ke depan, peningkatan performa model dapat dilakukan dengan **penambahan data pelatihan**, **pemilihan fitur yang lebih relevan**, serta **tuning arsitektur dan parameter model** secara lebih mendalam.
    """)

    st.subheader("Tech Stack yang Digunakan")
    st.write("""
    Berikut adalah daftar **alat**, **library**, dan **platform** yang digunakan dalam pengembangan aplikasi DiaDetect beserta fungsinya masing-masing:
    """)
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/python.svg", width=50)
    with col2:
        st.write("**Python**: Bahasa pemrograman utama untuk seluruh proses pengolahan data dan pembuatan model machine learning.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/tensorflow.svg", width=50)
    with col2:
        st.write("**TensorFlow**: Framework deep learning yang digunakan untuk membangun dan menyimpan model klasifikasi risiko diabetes.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/scikit-learn.svg", width=50)
    with col2:
        st.write("**Scikit-Learn**: Digunakan untuk preprocessing data, evaluasi metrik, dan transformasi standar (StandardScaler).")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/pandas.svg", width=50)
    with col2:
        st.write("**Pandas**: Library manipulasi data untuk pengolahan dan penyajian dataset tabular.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/numpy.svg", width=50)
    with col2:
        st.write("**NumPy**: Library numerik pendukung manipulasi array dan vektor dalam proses training dan inferensi.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/streamlit.svg", width=50)
    with col2:
        st.write("**Streamlit**: Framework Python yang digunakan untuk membangun aplikasi web interaktif berbasis model prediksi.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/colab.svg", width=50)
    with col2:
        st.write("**Google Colab**: Platform cloud notebook untuk proses pengembangan model dan eksperimen selama pelatihan.")
    col1, col2 = st.columns([1, 12], vertical_alignment="center")
    with col1:
        st.image("assets/kaggle.svg", width=50)
    with col2:
        st.write("**Kaggle BRFSS2015 Dataset**: Dataset utama yang digunakan untuk melatih model, diambil dari sumber resmi CDC.")

    st.subheader("Pengembang Aplikasi")
    st.write("""
    Proyek ini dibuat oleh dua mahasiswa yang memiliki latar belakang dalam bidang **Machine Learning**:
    """)

    col1, col2 = st.columns([1, 3.3])
    with col1:
        st.image("assets/yosua.svg", width=200)
    with col2:
        st.write("""
        ### **Yosua Samuel Edlyn Sinaga**  
        **Mahasiswa Teknik Informatika – Universitas Brawijaya**
        """)
        col1, col2, col3 = st.columns([0.1, 0.1, 1])
        with col1:
            st.markdown("""
            <a href="https://www.instagram.com/yyyosuaa" target="_blank">
                <img src="https://i.imgur.com/wbWav8i.png" width="30" alt="Instagram"/>
            </a>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <a href="https://github.com/yosuasinaga" target="_blank">
                <img src="https://i.imgur.com/HK87XAs.png" width="30" alt="GitHub"/>
            </a>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <a href="https://www.linkedin.com/in/yosua-sinaga" target="_blank">
                <img src="https://i.imgur.com/YmGmntc.png" width="30" alt="LinkedIn"/>
            </a>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3.3])
    with col1:
        st.image("assets/fachrul.svg", width=200)
    with col2:
        st.write("""
        ### **Fachrul Rozi Rangkuti**  
        **Mahasiswa Teknik Informatika – Politeknik Lhokseumawe Aceh**
        """)
        col1, col2, col3 = st.columns([0.1, 0.1, 1])
        with col1:
            st.markdown("""
            <a href="https://www.instagram.com/fachrlrzii_" target="_blank">
                <img src="https://i.imgur.com/wbWav8i.png" width="30" alt="Instagram"/>
            </a>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <a href="https://github.com/fachrulrozirangkuti" target="_blank">
                <img src="https://i.imgur.com/HK87XAs.png" width="30" alt="GitHub"/>
            </a>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <a href="https://www.linkedin.com/in/fachrul-rozi-rangkuti-01854a24a" target="_blank">
                <img src="https://i.imgur.com/YmGmntc.png" width="30" alt="LinkedIn"/>
            </a>
            """, unsafe_allow_html=True)

    st.subheader("Apresiasi dan Rencana Pengembangan Aplikasi")
    st.write("""
    Kami sangat menyadari bahwa aplikasi ini masih memiliki **banyak kekurangan**, baik dalam hal **fungsionalitas**, **kemudahan penggunaan**, maupun **akurasi prediksi** yang mungkin belum sempurna.  
    Kami mohon pengertiannya dan kami berkomitmen untuk terus **mengembangkan dan memperbaiki** aplikasi ini di masa depan agar lebih bermanfaat bagi semua pengguna.
    """)
    st.write("""
    **Terima kasih atas dukungan dan masukan Anda.**  
    Setiap umpan balik akan sangat membantu kami dalam **meningkatkan kualitas aplikasi ini**.
    """)
