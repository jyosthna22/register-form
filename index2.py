import streamlit as st

import streamlit as st

st.title(" Registration Form")

st.form("registration_form")
name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
gender = st.radio("Gender", ["Male", "Female", "Other"],index=None)
course = st.multiselect(
    "Select your course:",
    ["Python", "SQL", "Web Development", "Data Science","C","Java","c++","Data Analyst"]
)
agree = st.checkbox("I agree to the Terms & Conditions")

submit = st.button("Register")

if submit:
    st.success(f"Registration successful! Welcome, {name}.")


