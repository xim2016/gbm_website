import streamlit as st
 
st.markdown("<h2 style='text-align: center; color: black;'>Contact Us</h1>", unsafe_allow_html=True)  
a, b = st.columns([.3, .7])
b.markdown("""<div style="width: 100%"><iframe width="100%" height="700" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=5051%20Centre%20Avenue%20Pittsburgh,%20PA%2015213+(My%20Business%20Name)&amp;t=p&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"><a href="https://www.maps.ie/distance-area-calculator.html">measure distance on map</a></iframe></div>""", unsafe_allow_html=True)
a.image('https://wexfordscitech.com/wp-content/uploads/2021/03/Assembly-web-5.png')
a.markdown("""<span style="font-size:20px;">University of Pittsburgh, UPMC Hillman Cancer Center, Assembly Building</span>""", unsafe_allow_html=True)

#a.markdown('##### If you have any questions or feedback, please feel free to contact us:')
a.markdown("""<span style="font-size:18px;">Hatice Osmanbeyoglu<br>Principal Investigator<br>✉️ osmanbeyogluhu@pitt.edu</span>""", unsafe_allow_html=True)
a.markdown("""<span style="font-size:18px;">Linan Zhang<br>Assistant Professor<br>✉️ liz133@pitt.edu</span>""", unsafe_allow_html=True)
a.markdown("""<span style="font-size:18px;">Matthew Lu<br>Undergraduate Researcher<br>✉️ mal554@pitt.edu</span>""", unsafe_allow_html=True)
   