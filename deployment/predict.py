import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import joblib
import json

def run():
    # Membuat Form
    with st.form(key='form parameter'):
        Product_id = st.number_input('product_id', min_value=1, max_value=10000, step=1,)
        vendor_id = st.text_input('vendor_id', value='')
        country = st.text_input('country', value='')
        product_category = st.text_input('product_category', help='equipment, toys, snack, suplemment, bladding,')
        VAP = st.number_input('VAP', min_value=0, max_value=1, step=1, help='Approv Dokter? (0=Tidak perlu, 1=Perlu)')
        pet_size = st.selectbox('pet_size', ('extra small', 'small', 'medium', 'large', 'extra large'), index=1)
        pet_type = st.text_input('pet_type')
        rating = st.number_input('rating', min_value=1, max_value=10, step=1, help='rating 1 - 10')
        price = st.number_input('price', min_value=1, max_value=35000, step=1)
        sales = st.number_input('sales', min_value=1, max_value=500, step=1)
        st.markdown('---')

        submitted=st.form_submit_button('Predict')

    data_inf ={
            'product_id': Product_id,
            'product_category': product_category,
            'sales':sales,
            'price':price,
            'VAP':VAP,
            'vendor_id':vendor_id,
            'country':country,
            'pet_size':pet_size,
            'pet_type':pet_type,
            'rating':rating
        }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        X_inf = data_inf
        knn_pred = model_knn_reg.predict(X_inf)

        st.write('Re_buy:', str(int(knn_pred)))



