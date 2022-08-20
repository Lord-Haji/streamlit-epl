import streamlit as st
import soccerdata as sd
import streamlit_authenticator as stauth
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
     page_title="streamlit-epl",
     page_icon="⚽️",
     layout="wide",
     initial_sidebar_state="expanded"
 )
 
def epl():
     season = st.selectbox('Select EPL Season:',('2022','2021','2020'))
     five38 = sd.FiveThirtyEight('ENG-Premier League', season)
     games = five38.read_games()
     games_pr = games.profile_report()
     st_profile_report(games_pr)
 
page_names_to_funcs = {
     "EPL Analysis": epl   
}

selected_page = st.sidebar.selectbox("View", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
