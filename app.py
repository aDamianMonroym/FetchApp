import streamlit as st
import joblib
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly_express as px
import time


# Load the model
fetch_model = joblib.load(open("./Model/2022predictor_fetch-model.pkl", "rb"))

################### **Style**###################
icon = Image.open("Images/fetch-rewards.ico")
st.set_page_config(
    page_title="FetchApp",
    page_icon=icon,
    layout="wide",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.pixabay.com/photo/2016/10/29/09/48/abstract-1780242_1280.png");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
################### **Navigation Menu**###################

selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact", "Predictions"],
    icons=["house-door-fill", "file-earmark-person-fill",
           "person-lines-fill", "person-plus-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "cointainer": {"padding": "0!important"},
    }
)

################### **Selection**###################

if selected == "Home":
    header = st.container()

    with header:
        st.title("Fetch App")

        st.markdown(
            "The app for **_Machine_** **_Learning_** **_Models_** to predict the approximate number of scanned receipts")
        column1, column2, column3 = st.columns(3)
        with column2:
            img = Image.open("Images/Fetch.png")
            st.image(img, caption='©2023 Fetch')


if selected == "About":
    about = st.container()

    with about:
        st.title("About the app")
        col1, col2 = st.columns(2)
        with col1:
            for i in range(1):
                st.write("")
            st.markdown("""
                        #### FetchApp 
                         This **_web_** **_app_** allows the user to predict  the approximate number
                         of scanned receipts for each month of 2022. This app is also
                         part of the Take-home Exercise by Fetch Rewards ❤
                        """)

        with col2:
            img = Image.open("Images/1.jpg")
            st.image(img)

if selected == "Contact":
    contact = st.container()

    with contact:
        st.title("Contact")
        colu1, colu2 = st.columns(2)
        with colu1:
            for i in range(2):
                st.write("")

            st.markdown("""
                        * _Mechatronic_ _Engineer_ (10th Semester): Angel **_Damian_** Monroy Mendoza                    
                        * E-mail: adamianmm@gmail.com
                        * LinkedIn: linkedin.com/in/adamian-mm
                        * In love with Artificial Intelligence and Programming ❤
                        """)

        with colu2:
            img = Image.open("Images/FI.jpg")
            st.image(img)

if selected == "Predictions":
    st.title("Predictions")
    dataframe = pd.read_csv("./data_daily.csv")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("DataSet Visualization")
    col2.dataframe(dataframe)
    st.subheader("Dashboard: ")
    column4, column5, column6, column7, column8 = st.columns(5)
    with column5:
        with st.container():
            with st.spinner(text="Loading..."):
                time.sleep(3)
                st.success('Done')
                fig = px.line(dataframe, y='Receipt_Count',
                              x='# Date')
                fig.update_layout(title='Receipt Count 2021')
                st.plotly_chart(fig, theme="streamlit")

    with st.container():
        st.subheader("Predictions 2022: ")
        Month = st.slider("Select a month", 1, 12, value=1)
        WkE = st.selectbox("Is it a weekend?", ["Yes", "No"])
        if "button_clicked" not in st.session_state:
            st.session_state.button_clicked = False
        if "selected_month" not in st.session_state:
            st.session_state.selected_month = 1
        if "selected_wke" not in st.session_state:
            st.session_state.selected_wke = "Yes"

        def callback():
            st.session_state.button_clicked = True
            st.session_state.selected_month = int(Month)
            st.session_state.selected_wke = WkE

        if st.button("Predict", on_click=callback) or st.session_state.button_clicked:
            if st.session_state.selected_wke == "Yes":
                wk = 1
            else:
                wk = 0
            Prediction = pd.DataFrame({'Month': [int(st.session_state.selected_month)],
                                       'Weekend': [wk]})
            st.write("The prediction is: ")
            st.info(
                "With an algorithm which has an effectiveness of 91.74%, the Receipt Count for the Month " + str(st.session_state.selected_month) + " approximately is: ")
            col3, col4, col5 = st.columns(3)
            with col4:
                st.subheader(str(fetch_model.predict(
                    Prediction).round()[0][0]) + " tickets.")
        with st.container():
            img = Image.open("Images/Fetch2.png")
            st.image(img, caption='©2023 Fetch')
