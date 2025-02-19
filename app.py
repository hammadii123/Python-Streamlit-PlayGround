import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom CSS for a professional dark theme
st.markdown(
    """
    <style>
        body { background-color: #1E1E1E; color: white; }
        .stApp { background-color: #1E1E1E; }
        .main-title { color: #4DB6AC; font-size: 36px; text-align: center; font-weight: bold; }
        .input-box { background-color: #2C2C2C; color: white; border-radius: 8px; padding: 10px; }
        .stTextInput > div > div > input { background-color: #2C2C2C !important; color: white !important; }
        .stButton > button { background-color: #4DB6AC; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; }
        .stButton > button:hover { background-color: #00796B; }
        .result-text { font-size: 24px; font-weight: bold; text-align: center; padding: 10px; border-radius: 8px; }
        .normal { color: #4DB6AC; }
        .overweight { color: #FFA726; }
        .obese { color: #E53935; }
        .underweight { color: #42A5F5; }
        .footer { text-align: center; font-size: 14px; color: #BDBDBD; margin-top: 30px; }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<p class="main-title">⚖️ BMI Calculator</p>', unsafe_allow_html=True)



weight = st.text_input("Enter your weight (lbs)", placeholder="E.g., 150")
height = st.text_input("Enter your height (inches)", placeholder="E.g., 65")


#Calculation
if st.button("Calculate BMI"):
    if weight and height:
        try:
            weight = float(weight)
            height = float(height)

            if height > 0:
                bmi = weight * 703 / (height ** 2)

               
                if bmi < 18.5:
                    category = "Underweight 😕"
                    css_class = "underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal Weight 😊"
                    css_class = "normal"
                elif 25 <= bmi < 29.9:
                    category = "Overweight 😟"
                    css_class = "overweight"
                else:
                    category = "Obese 😞"
                    css_class = "obese"

                st.markdown(f'<p class="result-text {css_class}">Your BMI is: {round(bmi, 2)}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="result-text {css_class}">Category: {category}</p>', unsafe_allow_html=True)

            else:
                st.error("Height cannot be zero or negative!")

        except ValueError:
            st.error("Please enter valid numeric values for weight and height.")
    else:
        st.warning("Please enter both weight and height.")



st.markdown('<p class="footer">💡 A BMI between 18.5 and 24.9 is considered healthy.</p>', unsafe_allow_html=True)
