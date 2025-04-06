# Streamlit
import streamlit as st
import random

st.title("🪨📄✂️ Rock, Paper, Scissors")

user_choice = st.selectbox("Choose one:", ["rock", "paper", "scissors"])


if st.button("Play"):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    st.write(f"🤖 Computer chose: **{computer_choice}**")
    st.write(f"🧍 You chose: **{user_choice}**")

   
    if user_choice == computer_choice:
        st.info("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 You win!")
    else:
        st.error("💻 Computer wins!")



















# Normal Logic
import random

print("🪨 Rock, 📄 Paper, ✂️ Scissors Game!")
print("Choose: rock, paper, or scissors")


user_choice = input("Your choice: ").lower()


options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You win!")
else:
    print("💻 Computer wins!")
