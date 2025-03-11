import streamlit as st


length_units = {
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Micrometer": 1e6,
    "Nanometer": 1e9,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701,
    "LightYear": 1.057e-16
}

weight_units = {
    "Gram": 1,
    "Kilogram": 0.001,
    "Milligram": 1000,
    "Pound": 0.00220462,
    "Ounce": 0.035274
}

# Conversion functions
def convert_length(value, from_unit, to_unit):
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_weight(value, from_unit, to_unit):
    return value * (weight_units[to_unit] / weight_units[from_unit])




st.title("🌟Unit Converter")

category = st.selectbox("Select Category", ["Length", "Temperature", "Weight"])

if category == "Length":
    st.subheader("Length Converter")
    value = st.number_input("Enter Value", min_value=0.0, value=1.0, format="%.6f")
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

elif category == "Temperature":
    st.subheader("Temperature Converter")
    value = st.number_input("Enter Value", format="%.2f")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    st.subheader("Weight Converter")
    value = st.number_input("Enter Value", min_value=0.0, format="%.6f")
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

st.markdown("Made by : 'Hammad Mustafa' ")