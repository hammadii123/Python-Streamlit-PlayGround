# Streamlit Logic
import streamlit as st
import time

st.title("⏳ Easy Countdown Timer")


seconds = st.number_input("Enter time in seconds:", min_value=1)


if st.button("Start Timer"):
    # Empty space to show the timer
    timer_text = st.empty()


    for sec in range(seconds, 0, -1):
        mins = sec // 60
        secs = sec % 60
        timer_text.markdown(f"## 🕒 {mins:02d}:{secs:02d}")
        time.sleep(1)  
        

    st.success("🎉 Time's up!")






# Basic logic
# import time

# def countdown_timer(seconds):
#     while seconds > 0:
#         mins = seconds // 60
#         secs = seconds % 60
#         timer_format = f"{mins:02d}:{secs:02d}"
#         print(timer_format, end='\r')  
#         time.sleep(1)
#         seconds -= 1

#     print("Time's up! 🎉")


# countdown_timer(10)
