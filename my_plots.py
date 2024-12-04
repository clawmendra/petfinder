import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

adoptions = pd.read_csv('animals_data.csv')

# Filter by dogs and cats tabs
cats = adoptions[adoptions['species'] == 'Cat']
dogs = adoptions[adoptions['species'] == 'Dog']

st.selectbox = ("Filter by age range:",
                ("Baby", "Young", "Adult", "Senior"),
                )