import numpy as np
import pandas as pd
import streamlit as st
from my_plots import *

adoptions = pd.read_csv('animals_data.csv')

st.title('Pets Available for Adoption in UT')
# Filter by dogs and cats tabs
cats = adoptions[adoptions['species'] == 'Cat']
dogs = adoptions[adoptions['species'] == 'Dog']

tab1, tab2 = st.tabs(['Cats', 'Dogs'])

with tab1:
    age_selected = st.multiselect(
        "Select Age Range for Cats",
        ["Baby", "Young", "Adult", "Senior"]
    )
    genders = ['Male', 'Female']
    gender_option = st.radio(
        "Gender for Cat",
        genders
    )
    st.header(f'Distribution of {gender_option} Cats by Age')
    cat_fig = animal_plot(df=cats, sex=gender_option, ages=age_selected)
    st.plotly_chart(cat_fig)

with tab2:
    age_selected2 = st.multiselect(
        "Select Age Range for Dogs",
        ["Baby", "Young", "Adult", "Senior"]
    )
    genders2=['Male', "Female"]
    gender_option2 = st.radio(
        "Gender for Dog",
        genders2
    )
    
    st.header(f'Distribution of {gender_option} Dogs by Age')
    dog_fig = animal_plot(df=dogs, sex=gender_option2, ages=age_selected2)
    st.plotly_chart(dog_fig)

    # Sidebar Wideget
    st.sidebar.header('Give me a random pet!')
    if st.sidebar.button('Click Here', type = 'primary'):
        random_num = np.random.randint(0, len(adoptions))
        random_pet = adoptions.iloc[random_num]
        st.sidebar.write(f'Organization: {random_pet.iloc[-1]}')
        st.sidebar.write(f'Name: {random_pet.iloc[4]}')
        st.sidebar.write(f'Species: {random_pet.iloc[3]}')
        st.sidebar.write(f'Gender: {random_pet.iloc[-4]}')
        st.sidebar.write(f'Age: {random_pet.iloc[5]}')

    else:
        st.sidebar.write('')
  

