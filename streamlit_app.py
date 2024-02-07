import seaborn as sns
import numpy as np
import pandas as pd  
import streamlit as st  # pip install streamlit
import turtle 
import time
from pygame import mixer

st.set_page_config(page_title="Valentine", page_icon=":love icon:", layout="wide")

# ---- SIDEBAR ----
# st.sidebar.header("HI")



# ---- MAINPAGE ----
st.title("HAPPY VALENTINE")
st.markdown("##")

# Adding music is optional as per your choice.
# Initialize pygame mixer
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load('bensound-memories.mp3')

st.image('love.png')
mixer.music.play()



time.sleep(5)

st.markdown("##")


