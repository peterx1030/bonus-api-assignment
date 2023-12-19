import requests
import streamlit as st

st.image('https://images.ctfassets.net/hrltx12pl8hq/6TIZLa1AKeBel0yVO7ReIn/1fc0e2fd9fcc6d66b3cc733aa2547e11/weather-images.jpg?fit=fill&w=600&h=400')
st.title('Want to Check What to Wear?')

location = st.text_input("Enter a Place")

api_key = 'a68dff3935cfff9226e6d54b029bf059'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather_data(location, api_key):
    complete_url = f"{base_url}appid={api_key}&q={location}&units=imperial"  # Using imperial units for Fahrenheit
    response = requests.get(complete_url)
    return response.json()

def suggest_clothing(temperature):
    if temperature <= 45:
        return "It's chilly! Better wear a coat."
    elif 45 < temperature <= 60:
        return "A bit cool. A sweater would be good."
    elif temperature > 70:
        return "It's warm. A T-shirt would be comfortable."

if st.button('Check Weather'):
    if location:
        data = get_weather_data(location, api_key)
        if data['cod'] == 200:
            temp = data['main']['temp']
            st.write(f"Weather in {location}:")
            st.write(f"Temperature: {temp}°F")
            st.write(f"Weather: {data['weather'][0]['description']}")
            st.write(suggest_clothing(temp))
        else:
            st.error("Location not found. Please try again.")
    else:
        st.error("Please enter a location.")
