# Core Packages
import streamlit as st

# Applets
from eda_app import eda_main
from ml_app import ml_main

# Additional Packages
PAGE_CONFIG = {"page_title":"Text2Handwriting","page_icon":"https://img.icons8.com/doodle/48/000000/multi-edit--v1.png"}
st.set_page_config(**PAGE_CONFIG)

# Page Styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main Function
def main():
    local_css("style.css")

    Menu = ['EDA', 'ML']
    choice = st.sidebar.selectbox('Menu',Menu) 

    if choice == 'EDA':
        eda_main()
    elif choice == 'ML':
        ml_main()



if __name__ == '__main__':
    main()
