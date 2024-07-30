import streamlit as st
from VedicAstro import VedicHoroscopeData

# Define Streamlit app
st.title("Vedic Astrology with Streamlit")

# Input fields for date, time, and location
date = st.text_input("Date (YYYY-MM-DD)", "2024-07-30")
time = st.text_input("Time (HH:MM:SS)", "12:00:00")
latitude = st.number_input("Latitude", value=28.6139)
longitude = st.number_input("Longitude", value=77.2090)

if st.button("Calculate"):
    # Initialize VedicHoroscopeData
    vhd = VedicHoroscopeData(date=date, time=time, latitude=latitude, longitude=longitude)

    # Generate chart and get planetary positions
    chart = vhd.generate_chart()
    planets_data = vhd.get_planets_data_from_chart(chart)
    st.write("Planetary Positions:", planets_data)

    # Example for Vimshottari Dasa
    vimshottari_dasa = vhd.compute_vimshottari_dasa(chart)
    st.write("Vimshottari Dasa:", vimshottari_dasa)
