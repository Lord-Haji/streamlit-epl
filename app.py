import streamlit as st
import soccerdata as sd
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
from pivottablejs import pivot_ui

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
     games_pivot = pivot_ui(games)
     with open(t.src) as t:
         components.html(games_pivot.read(), width=900, height=1000, scrolling=True)
 
page_names_to_funcs = {
     "EPL Analysis": epl   
}

selected_page = st.sidebar.selectbox("View", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
