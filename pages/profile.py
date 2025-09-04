import streamlit as st
from streamlit_card import card

user_info = st.user.to_dict()

if user_info["is_logged_in"]:
    st.badge("Logged in", icon=":material/check:", color="green")
else:
    st.badge("Not Logged in", icon=":material/close:", color="red")

if not st.user.is_logged_in:
    st.error("Please login")

if st.user.is_logged_in:
    email = user_info["email"]
    email_verified = user_info["email_verified"]
    name = user_info["name"]
    image = user_info["picture"]

    user_card = card(
        title=f"Name: {name}",
        text=f"Email: {email}",
        image=image
    )

    if st.button("logout"):
        st.logout()