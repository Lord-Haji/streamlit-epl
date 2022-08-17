import streamlit as st
import soccerdata as sd

st.set_page_config(
     page_title="streamlit-soccer",
     page_icon="🚀",
     layout="wide",
     initial_sidebar_state="expanded"
 )
 
def home_page():
     season = st.st.selectbox('Select EPL Season:',('2022','2021','2020'))
     five38 = sd.FiveThirtyEight('ENG-Premier League', season)
     games = five38.read_games() 
     st.dataframe(games)
 
page_names_to_funcs = {
     "Home Page": home_page   
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
