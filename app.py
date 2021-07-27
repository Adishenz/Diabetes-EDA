# Core Packages
import streamlit as st

# Applets
from eda_app import eda_main
from ml_app import ml_main

# Additional Packages


# Page Styling
def page_styling():
    page_style = '''
    <style>
    .css-10trblm{
        text-align: center;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; 
        border: #f63366;
        border-style: double;
        border-radius: 10px;
        padding: 10px;
        }
    </st
    '''
    return page_style

# Main Function
def main():
    page_style = page_styling()
    st.markdown(page_style,unsafe_allow_html=True)

    Menu = ['EDA', 'ML']
    choice = st.sidebar.selectbox('Menu',Menu) 

    if choice == 'EDA':
        eda_main()
    elif choice == 'ML':
        ml_main()



if __name__ == '__main__':
    main()