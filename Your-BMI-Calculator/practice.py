import streamlit as st
st.title("BMI Calculator")
# st.button("Save")
weight=st.text_input("Enter the weight in Pounds:")

height=st.text_input("Enter the height in Inches:")

if st.button("Calculate the BMI"):
    if weight and height:
        try:
            weight = float(weight)
            height = float(height)

            if height > 0:
                bmi=weight*703/(height**2)
                st.write("Your BMI is: ", round(bmi,2))
            else:
                st.error("Invalid height")
        except ValueError:
            st.error("Please enter valid numeric values for weight and height.")
