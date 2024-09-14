import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/spatial_gene_tab/'

st.info('Insert Descrption')

file = open('text_files/spatial_gene_names_10.txt', 'r')
list = file.read().splitlines()

sample_list = ['MGH258', 'UKF243', 'UKF248', 'UKF251', 'UKF255', 'UKF259', 'UKF260',
                'UKF266', 'UKF269', 'UKF275', 'UKF296', 'UKF304', 'UKF313', 'UKF334',
                'ZH1007inf', 'ZH1007nec', 'ZH1019T1', 'ZH1019inf', 'ZH8811Abulk', 'ZH8811Bbulk',
                'ZH8812bulk', 'ZH881T1', 'ZH881inf', 'ZH916T1', 'ZH916bulk', 'ZH916inf']

a, b = st.columns(2)

option = a.selectbox(
    'Sample',
    sample_list) 

option2 = b.selectbox(
    'Gene',
    list) 

    
a.subheader('Spatial Plot')
a.image(f'{IMG_REPO}/spatial_expression/{option2}/{option}.png')
b.subheader('Violin Plot') 
b.image(f'{IMG_REPO}/violin_expression/{option2}/{option}.png')

st.info("Please Note: Only 10 genes listed for demo...full data will be pushed to GitHub asap")