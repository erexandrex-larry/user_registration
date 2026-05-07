import streamlit as st


st.title("User Registration")


first_name = st.text_input(
        label ="Frst name",
        placeholder = "Enter your first name",
        )


middle_name = st.text_input(
        label ="Middle name",
        placeholder = "Enter your middle name",
        )


last_name = st.text_input(
        label ="Last name",
        placeholder = "Enter your last name",
        )


email_address = st.text_input(
        label ="Email address",
        placeholder = "Enter your email address",
        )

name_of_institution = st.text_input(
        label ="Name of institution",
        placeholder = "Enter your name of your institution",
        )


name_lecturer = st.text_input(
        label ="Name of lecturer",
        placeholder = "Enter your lecturer name",
        )

residential_address = st.text_input(
        label ="residential address",
        placeholder = "Enter your residential address",
        )

cities_in_ghana = [
    "Accra",
    "Kumasi",
    "Tamale",
    "Takoradi",
    "Ashiaman",
    "Tema",
    "Cape Coast",
    "Obuasi",
    "Sunyani",
    "Sekondi-Takoradi",
]

city = st.selectbox(
        label ="City",
        options = cities_in_ghana,
        placeholder = "Select your city",
        )

button = st.button(
        label = "Register",
        key="register_button",
)
