import streamlit as st
from pint import UnitRegistry


ureg = UnitRegistry()


unit_categories = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot", "yard"],
    "Area": ["square meter", "square kilometer", "square mile", "acre"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "megabit/second", "gigabit/second"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Energy": ["joule", "calorie", "kilowatt hour"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["kilometers per liter", "miles per gallon"],
    "Mass": ["gram", "kilogram", "pound", "ounce"],
    "Plane Angle": ["degree", "radian"],
    "Pressure": ["pascal", "bar", "atm"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Volume": ["liter", "milliliter", "gallon"],
}


st.title("🔄 Universal Unit Converter")


category = st.selectbox("📌 Select a category:", list(unit_categories.keys()))


from_unit = st.selectbox("🔄 Convert from:", unit_categories[category])
to_unit = st.selectbox("🔄 Convert to:", unit_categories[category])


value = st.number_input("📝 Enter value:", min_value=1, step=1)


if st.button("🔄 Convert"):
    try:
        # Convert using pint
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"✅ {value} {from_unit} = {round(result.magnitude)} {to_unit}")
    except Exception as e:
        st.error(f"⚠️ Conversion error: {e}")

