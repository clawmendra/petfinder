import pandas as pd
import streamlit as st
import plotly.express as px

adoptions = pd.read_csv('animals_data.csv')

cats = adoptions[adoptions['species'] == 'Cat']
dogs = adoptions[adoptions['species'] == 'Dog']


def animal_plot(df, sex, ages):
    data = df.copy()

    if not ages:
        ages = ['Baby', 'Young', 'Adult', 'Senior']
    
    new_data = data[
        (data['gender'].str.contains(sex, case=False)) & 
        (data['age'].isin(ages))
    ]

    age_counts = new_data.groupby('age').size().reset_index()
    age_counts.columns = ['Age Range', 'Count']

    age_order = ["Baby", "Young", "Adult", "Senior"]
    age_counts['Age Range'] = pd.Categorical(age_counts['Age Range'], 
                                           categories=age_order, 
                                           ordered=True)
    pets = age_counts.sort_values('Age Range')

    fig = px.bar(
        pets,
        x='Age Range', 
        y='Count',
        title=f'Distribution of {sex} pets by Age',
        color='Age Range',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_layout(
        xaxis_title="Age Category",
        yaxis_title="Count",
        showlegend=False,
        plot_bgcolor='white',
        bargap=0.2
    )

    return fig