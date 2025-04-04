import streamlit as st
special_characters="!@#$%^&*"

def passwordCheck():
    has_upper=False
    has_lower=False
    has_number=False
    has_specialCharacters=False
    correct_length=False
    score = 0

    for x in password:
        if x.isupper():
            has_upper = True
        if x.islower():
            has_lower = True
        if x.isdigit():
            has_number = True
        if x in special_characters:
            has_specialCharacters = True

    if (len(password)>=8):
            score += 1
            correct_length=True

    
    if has_upper:
        score += 1
        st.write("Has Upper case✅")

    else:
        st.write("No upperCase❌ ")


    if  has_lower:
        score += 1
        st.write("Has LowerCase✅")

    else:
        st.write("No LowerCase❌ ")

    if has_number:
        score += 1
        st.write("Number✅")
    else:
        st.write("No numbers❌")

    if has_specialCharacters:
        score += 1
        st.write("Special characters✅")
    else:    
        st.write("Special characters❌")
       
  

    if correct_length:
        score+=1
        st.write("Length✅")
    else:    
        st.write("Length❌")
        


    st.write("Score=",score)


    if score >= 5:
        st.write("✅ Strong Password!")
    elif 3 <= score < 5:
        st.write("⚠️ Moderate Password - You can improve it.")
    else:
        st.write("❌ Weak Password - Needs improvement.")

password=st.text_input("Enter the Password:")

st.button("Check Password",on_click=passwordCheck)


st.badge("Made by : Hammad Mustafa", color="blue")





















# # Normal Logic:
# password = input("Enter the Password:")

# has_upper=False
# has_lower=False
# has_number=False
# has_specialCharacters=False
# correct_length=False
# score = 0

# special_characters="!@#$%^&*"
# for x in password:
#     if x.isupper():
#         has_upper = True
#     if x.islower():
#         has_lower = True
#     if x.isdigit():
#         has_number = True
#     if x in special_characters:
#         has_specialCharacters = True

# if (len(password)>=8):
#         score += 1
#         correct_length=True

   
# if has_upper and has_lower:
#     score += 1
#     print("Has Upper case and LowerCase both✅")

# else:
#     print("No upperCase❌ ")


# if  has_lower:
#     score += 1
#     print("Has LowerCase✅")

# else:
#     print("No LowerCase❌ ")

# if has_number:
#     score += 1
#     print("Number✅")
# else:
#     print("No numbers❌")

# if has_specialCharacters:
#     score += 1
#     print("Special characters✅")
# else:    
#     print("Special characters❌")


# print(score)
# if score == 5:
#     print("✅ Strong Password!")
# elif 3 <= score < 5:
#     print("⚠️ Moderate Password - You can improve it.")
# else:
#     print("❌ Weak Password - Needs improvement.")
