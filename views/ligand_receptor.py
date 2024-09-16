import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.info('Insert Descrption')

sample_list = ['MGH258', 'UKF243', 'UKF248', 'UKF251', 'UKF255', 'UKF259', 'UKF260',
                'UKF266', 'UKF269', 'UKF275', 'UKF296', 'UKF304', 'UKF313', 'UKF334',
                'ZH1007inf', 'ZH1007nec', 'ZH1019T1', 'ZH1019inf', 'ZH8811Abulk', 'ZH8811Bbulk',
                'ZH8812bulk', 'ZH881T1', 'ZH881inf', 'ZH916T1', 'ZH916bulk', 'ZH916inf']



option = st.selectbox(
    'Sample',
    sample_list) 


pdf_viewer(input = f'data/correlation_per_sample/{option}.pdf')