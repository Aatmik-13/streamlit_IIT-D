import streamlit as st
import time
from datetime import datetime, timedelta

today = datetime.today().date()

two_weeks_later = today + timedelta(weeks=2)

st.title("Book Reservation System")

with st.form("Book reservation form"):
    name = st.text_input("Enter your name")
    book = st.text_input("Enter the book name")
    author = st.text_input("Enter the author name")
    checkout_date = st.date_input("Enter the checkout date")
    submition_date = st.date_input("Select a date of submittion",     min_value=today, max_value=two_weeks_later)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Thank you for your reservation")
    st.write("Name:", name)
    st.write("Book:", book)
    st.write("Author:", author)
    st.write("Checkout Date:", checkout_date)
    st.write("Submittion Date:", submition_date)
