import streamlit as st
import pandas as pd
import random


st.set_page_config(page_title="Diet & Fitness Planner", page_icon="💪", layout="wide")


st.markdown("<h1 style='text-align: center; color: #ff4d4d;'>🥗 AI Diet & Fitness Planner 💪</h1>", unsafe_allow_html=True)
st.write("👋 Welcome! Get a **personalized 7-day meal & exercise plan** based on your weight.")


weight = st.slider("📏 Select your weight (kg):", min_value=30, max_value=150, value=70)


meals = {
    "Breakfast": ["🥣 Oatmeal with banana", "🍞 Scrambled eggs with toast", "🍯 Greek yogurt with honey", "🥤 Smoothie with protein", "🥞 Pancakes with peanut butter", "🍓 Fruit bowl with nuts", "🥑 Avocado toast"],
    "Lunch": ["🥗 Grilled chicken salad", "🍣 Salmon with quinoa", "🍛 Vegetable stir-fry with tofu", "🥘 Lentil soup with whole wheat bread", "🥩 Beef and brown rice bowl", "🍝 Pasta with spinach", "🐟 Grilled fish with sweet potato"],
    "Dinner": ["🐠 Grilled salmon with veggies", "🍗 Chicken breast with salad", "🍛 Vegetable curry with rice", "🥩 Beef steak with mashed potatoes", "🍲 Tofu stir-fry", "🍆 Eggplant lasagna", "🥖 Soup with whole-grain bread"]
}


exercises = {
    "Low Weight (<60kg)": {
        "Jump Rope": "1️⃣ Stand with feet together.\n2️⃣ Swing rope over your head & jump.\n3️⃣ Land softly & repeat.",
        "Bodyweight Squats": "1️⃣ Stand with feet shoulder-width apart.\n2️⃣ Lower hips until thighs are parallel to the floor.\n3️⃣ Push back up & repeat.",
        "Push-ups": "1️⃣ Place hands shoulder-width apart.\n2️⃣ Lower your chest until almost touching the ground.\n3️⃣ Push back up.",
    },
    "Medium Weight (60-90kg)": {
        "Weight Training": "1️⃣ Pick a comfortable weight.\n2️⃣ Perform curls, shoulder presses, & squats.\n3️⃣ Maintain control & proper form.",
        "Burpees": "1️⃣ Start in a squat position.\n2️⃣ Kick feet back into a push-up position.\n3️⃣ Jump back up and repeat.",
        "HIIT (15 min)": "1️⃣ Perform 30 sec sprints.\n2️⃣ Rest for 15 sec.\n3️⃣ Repeat 10-12 times.",
    },
    "High Weight (>90kg)": {
        "Brisk Walking": "1️⃣ Walk at a fast pace.\n2️⃣ Maintain a steady breath.\n3️⃣ Swing arms naturally.",
        "Water Aerobics": "1️⃣ Stand in water waist-deep.\n2️⃣ Move arms and legs against resistance.\n3️⃣ Perform kicks & arm circles.",
        "Yoga": "1️⃣ Sit comfortably & relax.\n2️⃣ Perform deep stretches.\n3️⃣ Breathe deeply & hold poses.",
    }
}


st.subheader("📅 Your Personalized 7-Day Plan")
plan = []
exercise_plan = []

for day in range(1, 8):
    plan.append({
        "Day": f"📆 Day {day}",
        "Breakfast": random.choice(meals["Breakfast"]),
        "Lunch": random.choice(meals["Lunch"]),
        "Dinner": random.choice(meals["Dinner"]),
    })

    if weight < 60:
        exercise = random.choice(list(exercises["Low Weight (<60kg)"].items()))
    elif 60 <= weight <= 90:
        exercise = random.choice(list(exercises["Medium Weight (60-90kg)"].items()))
    else:
        exercise = random.choice(list(exercises["High Weight (>90kg)"].items()))
    
    exercise_plan.append(exercise)



df = pd.DataFrame(plan)
st.table(df)


st.subheader("🏋️ Suggested Daily Exercise")
for day, (exercise, steps) in enumerate(exercise_plan, start=1):
    st.markdown(f"**📆 Day {day}: {exercise}**")
    st.text(steps)



st.sidebar.subheader("💪 Stay Motivated!")
quotes = [
    "🏆 Small steps every day lead to big results!",
    "💖 Your health is an investment, not an expense.",
    "🚀 One day or day one? You decide.",
    "🔥 Fitness is about being better than yesterday."
]
st.sidebar.write(random.choice(quotes))
