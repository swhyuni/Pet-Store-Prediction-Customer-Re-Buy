import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat title
    st.title('Prediksi Apakah konsumen akan membeli kembali produk')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisis Dataset')

    # Membuat Deskripsi
    st.write('Sri Wahyuni')

    # Menambahkan image
    image = Image.open('dataset-card.PNG')
    st.image(image, caption='Pet Store Record 2020')

    # Membuat garis lurus
    st.markdown('---')

    # Magic syntax
    '''
    Pada page kali ini, penulis akan melakukan eskplorasi sederhana.
    Dataset yang digunakan adalah dataset Pet Store Record 2020.
    yang diperoleh dari kaggle.
    '''

    # Show DataFrame
    data = pd.read_csv(r'C:\Users\wSatrian\github-classroom\H8-Assignments-Bay\p1---ftds-016-rmt--ml2-swhyuni\pet_store_records_2020.csv')
    st.dataframe(data)

    # Membuat barplot
    st.write('### Plot Re_Buy')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='re_buy', data=data)
    st.pyplot(fig)

    st.write('### Plot product_category')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='product_category', data=data)
    st.pyplot(fig)

    st.write('### Plot Rating')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='rating', data=data)
    st.pyplot(fig)

    # Membuat Histogram

    st.write('### Plot Histogram of Sales')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['sales'], bins=25 , kde=True)
    st.pyplot(fig)

    # Membuat Histogram berdasarkan input user
    st.write('### Histogram berdasarkan input user')
    pilihan = st.selectbox('Pilih Column: ', ('price', 'country', 'pet_size', 'pet_type'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=25 , kde=True)
    st.pyplot(fig)

if __name__== '__main__':
    run()