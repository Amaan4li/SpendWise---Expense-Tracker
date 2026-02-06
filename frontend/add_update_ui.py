import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"


def add_update_tap():
    selected_date = st.date_input("Enter the date", datetime(2025, 1, 1), label_visibility="collapsed", key="selected_date")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Failed to fetch data")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []  # to store the updated expense
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Food"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input("Amount", min_value=0.0, step=1.0, value=amount,
                                               key=f"amount_{selected_date}_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox("Category", options=categories, index=categories.index(category),
                                              key=f"category_{selected_date}_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input("Notes", value=notes, key=f"notes_{selected_date}_{i}",
                                            label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input,
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses Updated Successfully")
            else:
                st.error("Failed to update Expenses")
