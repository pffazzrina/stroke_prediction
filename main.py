# IMPORT LIBRARY
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import streamlit as st  # pip install streamlit

# LOAD MODEL
filename = 'finalized_model_rf.sav'
model = pickle.load(open(filename, 'rb'))

# MENGATUR PAGE
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Prediksi Penyakit Stroke", page_icon=":hearts:", layout="centered")

# MENGATUR JUDUL WEB APP
st.markdown('<div style="text-align: justify; font-size:210%"> <b>Stroke Prediction Web App</b> </div>',
            unsafe_allow_html=True)

# MENGATUR DESKRIPSI WEB APP
st.markdown('<div style="text-align: justify; font-size:160%"> Web App ini merupakan suatu aplikasi di mana kita bisa memprediksi apakah seseorang memiliki penyakit stroke berdasarkan beberapa variabel seperti BMI, usia, frekuensi merokok, dan lain sebagainya. </div>',
            unsafe_allow_html=True)

# MENULIS NAMA DEVELOPER
st.markdown('<hr>', unsafe_allow_html=True)
st.write("### Author : Putri Fazrina")
st.markdown('<hr>', unsafe_allow_html=True)

# MEMBUAT INPUT FORM
gender = st.selectbox('Apa Jenis Kelamin Anda?',
                      ('Laki-laki', 'Perempuan', 'Lainnya'))
usia = st.number_input(label = 'Berapa usia Anda?', min_value=18, max_value=100, step=1, key='1')
hipertensi = st.selectbox('Apakah Anda memiliki riwayat penyakit hipertensi?',
                          ('Ya', 'Tidak'))
heart_disease = st.selectbox('Apakah Anda memiliki riwayat penyakit jantung?',
                             ('Ya', 'Tidak'))
menikah = st.selectbox('Apakah Anda sudah menikah?',
                       ('Ya', 'Tidak'))
pekerjaan = st.selectbox('Apakah tipe pekerjaan Anda?',
                         ('Privat', 'Wiraswasta', 'Anak-anak', 'Pemerintah', 'Tidak Bekerja'))
tempattinggal = st.selectbox('Di mana Anda tinggal?',
                         ('Perkotaan', 'Pedesaan'))
glukosa = st.number_input(label = 'Berapa rata-rata kadar glukosa Anda?', min_value=0, max_value=500, step=10, key='2')
bmi = st.number_input(label = 'Berapa BMI Anda?', min_value=0, max_value=100, step=1, key='3')
merokok = st.selectbox('Apakah Anda seorang perokok?',
                       ('Ya, saya saat ini merokok', 'Ya, saya sebelumnya pernah merokok',
                        'Tidak merokok', 'Tidak tahu'))
st.markdown('<hr>', unsafe_allow_html=True)

# MENYIMPAN HASIL INPUT KE DALAM DATAFRAME
data = pd.DataFrame({'gender':[gender],
                     'age':[usia],
                     'hypertension':[hipertensi],
                     'heart_disease':[heart_disease],
                     'ever_married':[menikah],
                     'work_type':[pekerjaan],
                     'Residence_type':[tempattinggal],
                     'avg_glucose_level':[glukosa],
                     'bmi':[bmi],
                     'smoking_status':[merokok]})

# MELAKUKAN ENCODING
data['gender'] = data['gender'].replace('Laki-laki', 1)
data['gender'] = data['gender'].replace('Perempuan', 0)
data['gender'] = data['gender'].replace('Lainnya', 2)
data['hypertension'] = data['hypertension'].replace('Ya', 1)
data['hypertension'] = data['hypertension'].replace('Tidak', 0)
data['heart_disease'] = data['heart_disease'].replace('Ya', 1)
data['heart_disease'] = data['heart_disease'].replace('Tidak', 0)
data['ever_married'] = data['ever_married'].replace('Ya', 1)
data['ever_married'] = data['ever_married'].replace('Tidak', 0)
data['work_type'] = data['work_type'].replace('Privat', 2)
data['work_type'] = data['work_type'].replace('Wiraswasta', 3)
data['work_type'] = data['work_type'].replace('Anak-anak', 4)
data['work_type'] = data['work_type'].replace('Pemerintah', 0)
data['work_type'] = data['work_type'].replace('Tidak Bekerja', 1)
data['Residence_type'] = data['Residence_type'].replace('Perkotaan', 1)
data['Residence_type'] = data['Residence_type'].replace('Pedesaan', 0)
data['smoking_status'] = data['smoking_status'].replace('Ya, saya saat ini merokok', 3)
data['smoking_status'] = data['smoking_status'].replace('Ya, saya sebelumnya pernah merokok', 1)
data['smoking_status'] = data['smoking_status'].replace('Tidak merokok', 2)
data['smoking_status'] = data['smoking_status'].replace('Tidak tahu', 0)

# MENAMBAH SUBMIT BUTTON
submit = st.button("Submit")

# MELAKUKAN PREDIKSI
result_pred = model.predict(data.values)

# MENAMPILKAN HASIL
if submit:
    if result_pred[0] == 0:
        text = "Hasil Prediksi : Tidak Stroke"
        st.success(text)
    else:
        text = "Hasil Prediksi : Stroke"
        st.error(text)

