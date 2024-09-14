import streamlit as st


st.info('Insert Descrption')

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/spatial_pw_tab/'

file = open('text_files/spatial_pw_activity_names.txt', 'r')
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
    'Pathway',
    (list)) 

a.subheader('Spatial Plot')
a.image(f'{IMG_REPO}/spatial_pw_activity/HALLMARK_{option2}/{option}.png')
b.subheader('Violin Plot')
b.image(f'{IMG_REPO}/violin_pw_activity/HALLMARK_{option2}/{option}.png')


