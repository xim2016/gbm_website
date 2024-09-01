import streamlit as st
import hydralit_components as hc
from PIL import Image
#import streamlit_analytics

def home_page():

    #streamlit_analytics.start_tracking()
    #streamlit_analytics.stop_tracking()
    
    #img = "./data/Fig1_HomePage.png"

    st.markdown("<h2 style='text-align: center;  color: Black;'>Insert Title", unsafe_allow_html=True)
    st.write("")
    #st.image(img)
    st.markdown('➡️ Read our paper here: https://www.google.com')    
    st.write("Insert Description.")