import streamlit as st

# BACKGROUND_COLOR = 'white'
# COLOR = 'black'

st.info("Insert Description")
a, b, c, d, e= st.columns([5, 10, 10, 10, 10], gap = "medium")
a.markdown('##### No.')
b.markdown('##### Sample ID')
c.markdown('##### Cancer Type')
d.markdown('##### Accessible ID')
e.markdown('##### Date Published')

st.divider()
st.markdown("""
<style>
[role=radiogroup]{
   gap: 1rem;
}
</style>
""",unsafe_allow_html=True)

genre = a.radio(label = "dataset", label_visibility= 'collapsed', options = ['1', '2'])

st.markdown('##### Information')
if genre == '1':
   st.write("Sample ID: UFK241_C_ST")
   st.write("Dataset Name: GBM_Pmid35700707​")
   st.write("Cancer Type: GBM")
   st.write("Organ: Brain")
   st.write("Organ Detail: N/A")
   st.write("Sample Status: Normal Tissue")
   st.write("Platform: Visium")
   st.write("Mal-Bdy-nMal Axis: No")
   st.write("Accessible ID: Pmid: 35700707​")
   st.write("Date Published: 6/13/2022")
   st.markdown('##### DOI')
   st.markdown('https://doi.org/10.1016/j.ccell.2022.05.009')  
elif genre == '2':
   st.write("Sample ID: ")
   st.write("Dataset Name: ​")
   st.write("Cancer Type: ")
   st.write("Organ: ")
   st.write("Organ Detail: ")
   st.write("Sample Status: ")
   st.write("Platform: ")
   st.write("Mal-Bdy-nMal Axis: ")
   st.write("Accessible ID: Pmid: ​")
   st.write("Date Published: ")
   st.markdown('##### DOI')
   st.markdown('https://google.com')  

# -- TABLE --

b.write("UFK241_C_ST")
b.write("Sample")
c.write("GBM")
c.write("GBM")
d.write("Pmid: 35700707")
d.write("Pmid: 00000000")
e.write("6/13/2022")
e.write("1/1/2022")

st.info("Will turn into st.table for better appearance soon...")
     