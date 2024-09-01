import streamlit as st
import hydralit_components as hc




# BACKGROUND_COLOR = 'white'
# COLOR = 'black'


def datasets_page():

   
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
   
   genre = a.radio(label = "", label_visibility= 'collapsed', options = ['1'])
   
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
   
   
   # else:
   #    st.write("• All cells expressing <200 or >6,000 genes were removed, as well as cells that contained <400 (UMIs) and >15% mitochondrial counts.") 
   #    st.write("• The default parameters of Seurat were used, unless mentioned otherwise.")
   #    st.markdown('##### Reference')    
   #    st.markdown(f'[{"A single-cell map of intratumoral changes during anti-PD1 treatment of patients with breast cancer"}](https://www.nature.com/articles/s41591-021-01323-8)') 
   #    st.write("Bassez et al. Nat. Med. 2021")
   #    st.markdown('##### Data Source')
   #    st.markdown('https://lambrechtslab.sites.vib.be/en/single-cell')    
   
   b.write("UFK241_C_ST")
   c.write("GBM")
   d.write("Pmid: 35700707")
   e.write("6/13/2022")


     