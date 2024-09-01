import streamlit as st
import hydralit_components as hc
from PIL import Image

from home import home_page
from datasets import datasets_page
from metaprogram import metaprogram
from spatial_gene import spatial_gene
from spatial_tf import spatial_tf
from spatial_pathway import spatial_pathway
from ligand_receptor import ligand_receptor
from contact import contact_page


st.set_page_config(
        page_title='GBM',
        page_icon= "./logo/gbm_ribbon.png",
        initial_sidebar_state="expanded",
)

max_width_str = f"max-width: {85}%;"
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )

#Image.MAX_IMAGE_PIXELS = None

HOME = "Home"
DATA = "Datasets"
META = "Metaprogram"
GENE = "Spatial Gene Expression"
S_TF = "Spatial TF Activity"
S_PATHWAY = "Spatial Pathway Activity"
LIGAND = "Ligand-Receptor-TF-Pathway"
CONTACT = "Contact Us"

tabs = [
    HOME,
    DATA,
    META,
    GENE,
    S_TF,
    S_PATHWAY,
    LIGAND,
    CONTACT
]

option_data = [
    {'icon': "🏠", 'label':HOME},
    {'icon': "💾", 'label':DATA},
    {'icon': "💻", 'label':META},
    {'icon': "🧬", 'label':GENE},
    {'icon': "🔄", 'label':S_TF},
    {'icon': "👣", 'label':S_PATHWAY},
    {'icon': "📡", 'label':LIGAND},
    {'icon': "☎️", 'label':CONTACT}
]

theme = {'txc_inactive': 'white','menu_background':'#808080','txc_active':'black'}
chosen_tab = hc.nav_bar(menu_definition=option_data, override_theme = theme, use_animation= bool(True), 
    hide_streamlit_markers= bool(True))

if chosen_tab == HOME:
    home_page()

if chosen_tab == DATA:
    datasets_page()

elif chosen_tab == META:
    metaprogram()

elif chosen_tab == GENE:
    spatial_gene()

elif chosen_tab == S_TF:
    spatial_tf()

elif chosen_tab == S_PATHWAY:
    spatial_pathway()

elif chosen_tab == LIGAND:
    ligand_receptor()

elif chosen_tab == CONTACT:
    contact_page()



