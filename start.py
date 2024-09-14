import streamlit as st

# --- PAGE SETUP ----

st.set_page_config(
        page_title='GBM',
        page_icon= "./logo/gbm_ribbon.png",
        initial_sidebar_state="expanded",
)

max_width_str = f"max-width: {80}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )

home_page = st.Page(
    page = "views/home.py",
    title = "Home",
    icon = ":material/home:",
    default= True,
)

datasets_page = st.Page(
    page = "views/datasets.py",
    title = "Datasets",
    icon = ":material/dataset:"
)

metaprogram_page = st.Page(
    page = "views/metaprogram.py",
    title = "Metaprogram",
    icon = ":material/computer:"    
)

gene_page = st.Page(
    page = "views/spatial_gene.py",
    title = "Spatial Gene Expression",
    icon = ":material/genetics:"
)

s_tf_page = st.Page(
    page = "views/spatial_tf.py",
    title = "Spatial TF Activity",
    icon = ":material/cycle:"
)

s_pathway_page = st.Page(
    page = "views/spatial_pathway.py",
    title = "Spatial Pathway Activity",
    icon = ":material/footprint:"
)

ligand_page = st.Page(
    page = "views/ligand_receptor.py",
    title = "Ligand-Receptor-TF-Pathway",
    icon = ":material/settings_input_antenna:"
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact Us",
    icon = ":material/contact_page:"
)

# -- NAVIGATION --

pg = st.navigation(
    {
        "Menu": [home_page, datasets_page, metaprogram_page, gene_page, s_tf_page, s_pathway_page, ligand_page],
        "Contact": [contact_page]
    }
)


# -- SHARED ON ALL PAGES --
st.sidebar.text("Made by Osmanbeyoglu Lab")


# -- RUN NAVIGATION --
pg.run()




