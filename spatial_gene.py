import streamlit as st


def spatial_gene():
    st.info('Insert Descrption')

    sample_list = ["UKF275"]
    gene_list = ["CD44"]

    option = st.selectbox(
    'Sample',
    sample_list) 

    

    if option == 'UKF275':
        option2 = st.selectbox(
        'Gene',
        gene_list) 
        
    if option2 == 'CD44':
            
            a, b = st.columns(2)
            a.subheader('Spatial Plot')
            a.image('./images/gene_expression/Picture5.png')
            b.subheader('Violin Plot') 
            b.image('./images/gene_expression/Picture6.png')
