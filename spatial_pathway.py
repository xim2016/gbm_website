import streamlit as st


def spatial_pathway():
    st.info('Insert Descrption')

    sample_list = ["UKF248"]
    pw_list = ["Cholesterol Homeostasis"]

    option = st.selectbox(
    'Sample',
    sample_list) 

    

    if option == 'UKF248':
        option2 = st.selectbox(
        'Pathway',
        pw_list) 
        
    if option2 == 'Cholesterol Homeostasis':
            
            a, b = st.columns(2)
            a.subheader('Spatial Plot')
            a.image('./images/pw_activity/Picture9.png')
            b.subheader('Violin Plot')
            b.image('./images/pw_activity/Picture10.png')


