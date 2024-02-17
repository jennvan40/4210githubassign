import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see Kart or racer stats")

link = '[To my GitHub Pages Site](https://jennvan40.github.io/4210githubassign/)'
st.markdown(link, unsafe_allow_html=True)
