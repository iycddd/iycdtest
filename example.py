from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
import chime

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)


if st.button("sound"):
  chime.success()
  chime.info(sync=True)
