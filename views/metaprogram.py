import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/metaprogram_tab/'

st.info('Insert Descrption')
sample_list = ['MGH258', 'UKF243', 'UKF248', 'UKF251', 'UKF255', 'UKF259', 'UKF260',
                'UKF266', 'UKF269', 'UKF275', 'UKF296', 'UKF304', 'UKF313', 'UKF334',
                'ZH1007inf', 'ZH1007nec', 'ZH1019T1', 'ZH1019inf', 'ZH8811Abulk', 'ZH8811Bbulk',
                'ZH8812bulk', 'ZH881T1', 'ZH881inf', 'ZH916T1', 'ZH916bulk', 'ZH916inf']
list2 = ["Neuron"]

option = st.selectbox(
    'Sample',
    sample_list) 

a, b, c, d = st.columns([.33, .24, .2, .05])


a.markdown("<h3 style='text-align: center; color: black;'>Metaprograms</h1>", unsafe_allow_html=True)
b.markdown("<h3 style='text-align: center; color: black;'>Metaprogram Proportion</h1>", unsafe_allow_html=True)
c.markdown("<h3 style='text-align: center; color: black;'>HE Stain</h1>", unsafe_allow_html=True)


a.image(f'{IMG_REPO}/metaprogram/{option}.png')
b.image(f'{IMG_REPO}/pie_metaprogram/{option}.png')
c.image(f'{IMG_REPO}/he_stain/{option}.png')


# -- Single Metaprogram Images --

#Error with blank images

col1, col2, col3 = st.columns(3)
col1.subheader('Single Metaprogram')
col2.subheader('')
col3.subheader('')

col1.image(f'{IMG_REPO}/metaprogram_AC/{option}.png')
col2.image(f'{IMG_REPO}/metaprogram_Chromatin.Reg/{option}.png')
col3.image(f'{IMG_REPO}/metaprogram_Inflammatory.Mac/{option}.png')
col1.image(f'{IMG_REPO}/metaprogram_MES.Ast/{option}.png')
col2.image(f'{IMG_REPO}/metaprogram_MES.Hyp/{option}.png')
col3.image(f'{IMG_REPO}/metaprogram_MES/{option}.png')
col1.image(f'{IMG_REPO}/metaprogram_Mac/{option}.png')
col2.image(f'{IMG_REPO}/metaprogram_NPC/{option}.png')
col3.image(f'{IMG_REPO}/metaprogram_Neuron/{option}.png')
col1.image(f'{IMG_REPO}/metaprogram_OPC/{option}.png')
col2.image(f'{IMG_REPO}/metaprogram_Oligo/{option}.png')
col3.image(f'{IMG_REPO}/metaprogram_Prolif.Metab/{option}.png')
col1.image(f'{IMG_REPO}/metaprogram_Reactive.Ast/{option}.png')
col2.image(f'{IMG_REPO}/metaprogram_Vasc/{option}.png')

