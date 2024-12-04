import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

adoptions = pd.read_csv('animals_data.csv')

st.title('Pet Available for Adoption in UT')

tab1, tab2 = st.tabs(['Cats', 'Dogs'])

with tab1:
    st.write("Select Age")