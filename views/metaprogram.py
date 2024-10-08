import streamlit as st
import hydralit_components as hc

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/metaprogram_tab/'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/dotplot_tf_activity'

st.info('Insert Descrption')
sample_list = ['MGH258', 'UKF243', 'UKF248', 'UKF251', 'UKF255', 'UKF259', 'UKF260',
                'UKF266', 'UKF269', 'UKF275', 'UKF296', 'UKF304', 'UKF313', 'UKF334',
                'ZH1007inf', 'ZH1007nec', 'ZH1019T1', 'ZH1019inf', 'ZH8811Abulk', 'ZH8811Bbulk',
                'ZH8812bulk', 'ZH881T1', 'ZH881inf', 'ZH916T1', 'ZH916bulk', 'ZH916inf']

option_data = [
{'icon': "", 'label':i} for i in ['Metaprogram Overview', 'Metaprogram TF Activity']]

over_theme = {'txc_inactive': 'black','menu_background':'#A9A9A9','txc_active':'black','option_active':'#F0F2F6'}

page = hc.option_bar(
    option_definition=option_data,
    title='',
    override_theme=over_theme,
    horizontal_orientation=True,
    )

if page == 'Metaprogram Overview':

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


    a.text("")
    a.text("")
    a.text("")

    col1, col2, col3 = st.columns(3)


    a.markdown("<h3 style='text-align: center; color: black;'>Single Metaprogram</h1>", unsafe_allow_html=True)
    b.markdown("<h3 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
    c.markdown("<h3 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)

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

else:

    option_2 = st.selectbox(
    'Sample',
    sample_list) 

    st.image(f'{IMG_REPO_2}/{option_2}.png')

