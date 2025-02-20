import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
# Load API key securely from secrets.toml
api_key = st.secrets["OPENWEATHER_API_KEY"]

# Set page config
st.set_page_config(page_title="Weather Forecast App", layout="wide")

import streamlit as st

# Hide Streamlit's branding (GitHub icon, Fork icon, and Footer)
hide_streamlit_style = """
    <style>
        MainMenu {visibility: hidden;} /* Hide hamburger menu */
        footer {visibility: hidden;} /* Hide footer */
        header {visibility: hidden;} /* Hide header */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Custom CSS for better UI
st.markdown("""
    <style>
            
    .stTextInput>div>div>input {
        color: #4F8BF9;
        font-size: 18px;
    }
    .stMarkdown h1 {
        color: #4F8BF9;
    }
    .stMarkdown h2 {
        color: #4F8BF9;
    }
    .stMarkdown h3 {
        color: #4F8BF9;
    }
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        font-size: 18px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stAlert {
        background-color: #FFCCCB;
        color: #D8000C;
    }
    </style>
    """, unsafe_allow_html=True)

# Main app
st.title("🌤️ Weather Forecast App")
st.markdown("### Enter a city name to get the current weather and 5-day forecast")

city = st.text_input("Enter city name", "Karachi")

if api_key and city:
    try:
        # Get current weather data
        current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        current_response = requests.get(current_url)
        current_data = current_response.json()

        if current_data['cod'] == 200:
            # Display current weather
            st.markdown(f"### 🌍 Weather in {city.title()}")
            col1, col2, col3, col4 = st.columns(4)
            temp_celsius = round(current_data['main']['temp'], 1)
            humidity = current_data['main']['humidity']
            description = current_data['weather'][0]['description'].title()
            icon_code = current_data['weather'][0]['icon']
            
            with col1:
                st.markdown("**Temperature**")
                st.markdown(f"<h1 style='color:#4F8BF9;'>{temp_celsius}°C</h1>", unsafe_allow_html=True)
            with col2:
                st.markdown("**Humidity**")
                st.markdown(f"<h1 style='color:#4F8BF9;'>{humidity}%</h1>", unsafe_allow_html=True)
            with col3:
                st.markdown("**Conditions**")
                st.markdown(f"<h1 style='color:#4F8BF9;'>{description}</h1>", unsafe_allow_html=True)
            with col4:
                st.markdown("**Icon**")
                st.image(f"http://openweathermap.org/img/wn/{icon_code}@2x.png", width=100)

            # Get forecast data
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            if forecast_data['cod'] == '200':
                # Process forecast data
                forecast_list = forecast_data['list']
                dates = []
                temps = []
                
                for entry in forecast_list:
                    dt = datetime.fromtimestamp(entry['dt'])
                    dates.append(dt)
                    temps.append(round(entry['main']['temp'], 1))

                # Create DataFrame for plotting
                df = pd.DataFrame({'Date': dates, 'Temperature': temps})
                
                # Plot temperature trends
                st.markdown(f"### 📈 5-Day Temperature Forecast for {city.title()}")
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='#4F8BF9')
                ax.set_xlabel("Date", fontsize=12)
                ax.set_ylabel("Temperature (°C)", fontsize=12)
                ax.grid(True, linestyle='--', alpha=0.7)
                plt.xticks(rotation=45, fontsize=10)
                plt.yticks(fontsize=10)
                st.pyplot(fig)
            else:
                st.error("Error fetching forecast data")
        else:
            st.error("City not found. Please try again.")
    
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")

elif not api_key:
    st.warning("API key is missing. Please configure it in the .env file.")