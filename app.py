import streamlit as st
import soccerdata as sd
import streamlit_authenticator as stauth
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
     page_title="Sports Guru",
     page_icon="⚽️",
     layout="wide",
     initial_sidebar_state="expanded"
 )
 
def epl():
     league = st.selectbox('Select League:',('EPL','La Liga', 'Ligue 1', 'Bundesliga', 'Serie A'))
     # if league == 'World Cup':
     #      season = st.selectbox('Select Edition:',('2022','2018','2014'))
     # else:

     season = st.selectbox('Select Season:',('2022','2021','2020'))

     # if league == 'World Cup':
     #      leaguestring = 'INT-World Cup'

     if league == 'EPL':
          leaguestring = 'ENG-Premier League'

     elif league == 'La Liga':
          leaguestring = 'ESP-La Liga'
     
     elif league == 'Ligue 1':
          leaguestring = 'FRA-Ligue 1'

     elif league == 'Bundesliga':
          leaguestring = 'GER-Bundesliga'

     elif league == 'Serie A':
          leaguestring = 'ITA-Serie A'

     five38 = sd.FiveThirtyEight(leaguestring, season)
     games = five38.read_games()
     games_pr = games.profile_report()
     st_profile_report(games_pr)
 
page_names_to_funcs = {
     "Soccer Analysis": epl   
}

selected_page = st.sidebar.selectbox("View", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
