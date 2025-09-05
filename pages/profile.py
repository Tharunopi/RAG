import streamlit as st
from streamlit_card import card
from utils.supabase import supabaseClient, userData

if st.session_state["is_logged_in"]:
    st.badge("Logged in", icon=":material/check:", color="green")
else:
    st.badge("Not Logged in", icon=":material/close:", color="red")

if not st.user.is_logged_in:
    st.error("Please login")

if st.user.is_logged_in:
    name = st.session_state["name"]
    email = st.session_state["email"]
    image = st.session_state["image"]
    email_verified = st.session_state["email_verified"]

    user_card = card(
        title=f"Name: {name}",
        text=f"Email: {email}",
        image=image
    )

    supabase = supabaseClient()
    if "logged_into_supabase_db" not in st.session_state:
        st.session_state["logged_into_supabase_db"] = True
        db_user_data = userData(name=name, email_id=email, email_verified=email_verified, profile_icon=image)
        upsert_result = supabase.upsert(db_user_data)

    if st.button("logout"):
        st.logout()