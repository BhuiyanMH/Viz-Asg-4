import pandas as pd
import streamlit as st
import altair as alt

#load gender data with the continent column
gender_data = pd.read_csv('gender_with_continent.csv')

chart = alt.Chart(gender_data).mark_line().encode(
    alt.X('Year:O'),
    alt.Y('median(Fertility rate, total (births per woman)):Q',
          title='Median of Fertility Rate'
          ),
    alt.Color('Continent:N', scale=alt.Scale(scheme='tableau10'))
).transform_filter('datum.Year != 2017').properties(
    title={
      "text": ["Trend in Fertility Rate of Different Continents with Time"],
      "subtitle": ["All the continents have seen big drop in fertility rate except Europe during the time 1960 to 2016.","The fertility rate of Europe was less than half of that of Africa during 1960 and ended up almost at the same point in 2016."]
    },
    width=1000,
    height=400,
    padding={'left': 10, 'top': 10, 'right': 10, 'bottom': 10}
).configure_title(
    fontSize=18,
    font='Courier',
    anchor='start',
    color='black',
    subtitleColor='gray',
    offset=16,
    dx=24
)
st.write(chart)
chart.save('BHUIYAN-Gender-P1.png')