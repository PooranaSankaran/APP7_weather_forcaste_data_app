import streamlit as st
import plotly.express as px
from backend import get_data

#Add title, text, input, slider, sselectbox, and subheader
st.title('Weather Forcast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcaste Days', min_value=1, max_value=5,
                 help='select the number of forcasted days') # slider = adjust dates in UI
options = st.selectbox('Select data to view',
                       ('Temperature', 'Sky'))
st.subheader(f"{options} for the next {days} days in {place}")
#eg: output wil be Temperature for the next 2 days in india.

if place:

#visualization
# get temp data
    try:
        filtered_data = get_data(place, days)

        if options == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x = dates , y = temperatures) # line plot
            st.plotly_chart(figure)

        if options=='Sky':
            images = {'Clear':'images/clear.png','Clouds':'images/cloud.png',
                      'Rain':'images/rain.png', 'snow':'images/snow.png'}
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width= 115)
    except:
        st.write('That place doesnot exit')