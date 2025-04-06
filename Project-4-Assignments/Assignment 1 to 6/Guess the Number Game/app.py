import streamlit as st
import random

st.title("🎯 Guess the Number")


if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)
    st.session_state.count = 0


guess = st.number_input("Guess a number (1-10):", 1, 10)


if st.button("Guess"):
    st.session_state.count += 1

    if guess == st.session_state.number:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error("❌ Try again!")

# Show tries
st.write("Tries:", st.session_state.count)

# Reset
if st.button("Reset Game"):
    st.session_state.number = random.randint(1, 10)
    st.session_state.count = 0


















# Normal Logic
# import random

# # Step 1: Generate a random number
# secret_number = random.randint(1, 100)
# max_attempts = 10

# print("🎯 Welcome to Guess the Number Game!")
# print("I'm thinking of a number between 1 and 100.")
# print(f"You have {max_attempts} attempts to guess it!")


# for attempt in range(1, max_attempts + 1):
#     guess = int(input(f"Attempt {attempt}: Enter your guess: "))

#     if guess < secret_number:
#         print("Too low! Try again.\n")
#     elif guess > secret_number:
#         print("Too high! Try again.\n")
#     else:
#         print(f"🎉 Correct! You guessed it in {attempt} attempts.")
#         break
# else:
#     print(f"😢 Sorry! You ran out of attempts. The number was {secret_number}.")
