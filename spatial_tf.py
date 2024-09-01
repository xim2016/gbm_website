import streamlit as st


def spatial_tf():
    st.info('Insert Descrption')

    sample_list = ["UKF248"]
    tf_list = ["AR"]

    option = st.selectbox(
    'Sample',
    sample_list) 

    

    if option == 'UKF248':
        option2 = st.selectbox(
        'TF',
        tf_list) 
        
    if option2 == 'AR':
            
            a, b = st.columns(2)
            a.subheader('Spatial Plot')            
            a.image('./images/tf_activity/Picture7.png')
            b.subheader('Violin Plot')
            b.image('./images/tf_activity/Picture8.png')