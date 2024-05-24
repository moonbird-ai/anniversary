from openai import OpenAI
import streamlit as st
from functions import *
client = OpenAI(api_key=st.secrets["open_ai"])
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("happy anniversary, julie")

# anniversaryMessage = toast("joyful")
# toastContainer = st.empty()
# toastContainer.write(anniversaryMessage)
st.header("people from all over the world are here to celebrate our decade of marriage! they are lined up to propose toasts.")
newTone = st.text_input("who would you like to hear a toast from?", help="think of ANYTHING your imagination can conjure. be creative. celebrities. random nationalities. people doing something funny.")
if st.button("clink!"):
    col1, col2 = st.columns(2)
    with col1:
        st.write(toast(newTone))
    with col2:
        st.image(imageMaker(newTone))

st.divider()
