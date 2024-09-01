import streamlit as st


def metaprogram():

    st.info('Insert Descrption')

    sample_list = ["UKF266"]
    list2 = ["Neuron"]
    

    option = st.selectbox(
    'Sample',
    sample_list) 

    a, b, c = st.columns(3)

    if option == 'UKF266':
        a.subheader('HE Stain')
        a.image('./images/metaprogram/Picture1.png')
        b.subheader('Metaprogram Proportion')
        b.image('./images/metaprogram/Picture4.png')
        c.subheader('Metaprograms')
        c.image('./images/metaprogram/Picture2.png')
       
        
        st.subheader('Single Metaprogram')

        option2 = st.selectbox(
            '___',
            list2) 
        
        if option2 == 'Neuron':
            st.image('./images/metaprogram/Picture3.png')
