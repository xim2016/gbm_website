import streamlit as st
import hydralit_components as hc
from streamlit_pdf_viewer import pdf_viewer


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/dotplot_tf_activity'

st.info('Insert Descrption')

file = open('text_files/dotplot_tf_names.txt', 'r')
list = file.read().splitlines()

file2 = open('text_files/correlation_per_gene_names.txt', 'r')
list2 = file2.read().splitlines()


option_data = [
{'icon': "", 'label':i} for i in ['TF Activity', 'Pathway']]

over_theme = {'txc_inactive': 'black','menu_background':'#A9A9A9','txc_active':'black','option_active':'#F0F2F6'}

page = hc.option_bar(
    option_definition=option_data,
    title='',
    override_theme=over_theme,
    horizontal_orientation=True,
    )

if page == 'TF Activity':

    option = st.selectbox(
    'Sample',
    list) 

    st.image(f'{IMG_REPO}/{option}.png')

else:
    option2 = st.selectbox(
    'Sample',
    list2) 

    pdf_viewer(input = f'data/correlation_per_gene/{option2}.pdf')
