import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('gender_with_continent.csv', index_col = False)
df_recent = df[(df['Year'] >= 2000)&(df['Year'] < 2017)]
df_2016 = df_recent[df_recent.Year == 2016]
df_2016_unemployment = df_2016[['Continent', 'Country Name', 'Unemployment, youth female (% of female labor force ages 15-24) (modeled ILO estimate)', 'Unemployment, youth male (% of male labor force ages 15-24) (modeled ILO estimate)']]
df_2016_unemployment.columns = ['Continent', 'Country', 'Female', 'Male']

#Melt the Male/Female columns to a single Sex column
df_2016_unemployment = pd.melt(df_2016_unemployment, id_vars=['Continent', 'Country'], value_vars=['Male', 'Female'], var_name='Sex', value_name='Unemployment Rate')

chart = alt.Chart(df_2016_unemployment)
chart = alt.Chart(df_2016_unemployment).mark_bar().encode(
    alt.X('Sex:N', axis=None),
    alt.Y('mean(Unemployment Rate):Q',
          title='Average of Unemployment Rate',
          scale=alt.Scale(domain=[10, 22]),
          axis=alt.Axis(grid=False)
          ),
    alt.Column('Continent:N'),
    alt.Color('Sex:N')
).properties(
    title='Variation of youth unemployment rate among continents'
).configure_title(
    fontSize=16,
    anchor='middle',
    color='gray'
)
st.write(chart)
chart.save('BHUIYAN-Gender-P2.png')